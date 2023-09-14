from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from settings import admins, baza_task, baza_info, logs
from bot_logic import Access, log, id_from_text, FSM, get_tsv, accept_user
from lexic import lex
import json
import os
from config import Config, load_config
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

# import pygsheets
# import googleapiclient.errors


# Инициализация
router: Router = Router()
config: Config = load_config()
TKN: str = config.tg_bot.token


# # Забанить юзера по telegram id. Пример сообщения: ban id123456789
# @router.message(Access(admins), lambda msg: str(msg.text).lower().startswith('ban '))
# async def banner(msg: Message):
#     # вытащить id из текста сообщения
#     ban_id = str(msg.text).split()[-1]
#     if ban_id.lower().startswith('id'):
#         ban_id = ban_id[2:]
#
#     log('user_status.json', 'ban', ban_id)
#     await msg.answer(text=f'id {ban_id} banned')


# admin нажал ✅
@router.callback_query(Access(admins), lambda x: x.data == 'admin_ok')
async def admin_ok(callback: CallbackQuery, bot:Bot):
    msg = callback.message

    # worker = вытащить id из текста сообщения
    worker = id_from_text(msg.text)

    # принять все файлы
    await accept_user(TKN, bot, worker)
    log(logs, worker, 'admin_accept')

    # убрать кнопки админа
    await bot.edit_message_text(f'{msg.text}\n✅ Принято', msg.chat.id, msg.message_id, reply_markup=None)
    # Дать юзеру аппрув
    await bot.send_message(chat_id=worker, text=lex['all_approved']+f'id{worker}')
    log(logs, worker, 'admin_accept')
    # # сохранить ссылки
    # gc = pygsheets.authorize(service_file='token.json')
    # sheet_url = 'https://docs.google.com/spreadsheets/d/1dlZdboea3OAzNpivRxgDiQ6SaW14RjHdfFD-77HwGiQ/edit#gid=0'
    # spreadsheet = gc.open_by_url(sheet_url)
    # try:
    #     spreadsheet.add_worksheet(title=worker)
    # except googleapiclient.errors.HttpError:
    #     pass

    # сохранить ссылки в g_sheet, в отдельный tsv и print в консоль

    path = await get_tsv(TKN, bot, msg, worker)
    # отправить tsv админу
    for i in admins:
        await bot.send_document(chat_id=i, document=FSInputFile(path=path))


# admin нажал ❌
@router.callback_query(Access(admins), lambda x: x.data == 'admin_no')
async def admin_no(callback: CallbackQuery, bot: Bot):
    msg = callback.message

    # обновить сообщение у админа и убрать кнопки
    await bot.edit_message_text(f'{msg.text}\n\n❌ Отклонено. Напиши причину отказа '
                                f'для каждого файла <b>одним ответом на это сообщение</b>!\n\n'
                                f'Укажи номер задания и через пробел причину. Следующее задание '
                                f'- перенос строки. Например:\n'
                                f'\n<i>05 плохое качество'
                                f'\n51 обрезано лицо</i>',
                                msg.chat.id, msg.message_id, parse_mode='HTML', reply_markup=None)


# админ ответил на сообщение
@router.message(Access(admins), lambda msg: msg.reply_to_message)
async def reply_to_msg(msg: Message, bot: Bot):
    # ответ админа
    admin_response = str(msg.text)
    # сообщение, на которое отвечает админ
    orig = msg.reply_to_message

    # worker = вытащить id из текста сообщения
    worker = id_from_text(orig.text)
    txt_for_worker = '\n\n'

    # если админ тупит
    if not worker:
        await bot.send_message(orig.chat.id, 'На это сообщение не надо отвечать')

    # если админ написал причину отказа❌
    elif lex["adm_review"] in orig.text:
        print('adm reject')
        # записать номера отклоненных файлов
        rejected_files = []
        correct_format = True
        for line in admin_response.split('\n'):
            print(line)
            file_num = line.split()[0]
            # убедиться, что каждая строка начинается с номера задания
            if not file_num.isnumeric():
                correct_format = False
                await bot.send_message(orig.chat.id, lex['wrong_rej_form'])
                break
            rejected_files.append(line.split()[0])
            txt_for_worker += 'Задание '+line+'\n'

        if correct_format:
            # прочитать данные юзера из пд
            with open(baza_info, 'r', encoding='utf-8') as f:
                data_inf = json.load(f)
            # if worker not in data_inf:
            #     print(worker, 'new user from:', None)
                # data_tsk.setdefault(worker, lex['user_account'])
                #
                # # создать запись ПД
                # print(user_id, 'pd created')
                # info = lex['user_pd']
                # info['referral'] = None
                # info['first_start'] = None
                # info['tg_username'] = message.from_user.username
                # info['tg_fullname'] = message.from_user.full_name
                # print(info)
                # data_inf.setdefault(worker, info)

            if worker in data_inf:
                ref = data_inf[worker]['referral']
                username = data_inf[worker]['tg_username']
                fullname = data_inf[worker]['tg_fullname']
            else:
                ref = username = fullname = '?'

            # обновить сообщение у админа и дописать причину отказа
            await bot.edit_message_text(f'❌ Отклонено. Причина:\n{admin_response}', orig.chat.id, orig.message_id,
                                        reply_markup=None)
            # продублировать всем админам
            for i in admins:
                await bot.send_message(chat_id=i, text=f'❌ Отклонено.\nid{worker} {fullname} @{username} ref: {ref}'
                                                       f'\nПричина:\n{admin_response}')
            # сообщить юзеру об отказе
            msg_to_pin = await bot.send_message(chat_id=worker, text=lex['reject']+f'<i>{txt_for_worker}</i>', parse_mode='HTML')
            await bot.pin_chat_message(message_id=msg_to_pin.message_id, chat_id=worker, disable_notification=True)

            # проставить reject в отклоненных файлах
            with open(baza_task, 'r', encoding='utf-8') as f:
                data = json.load(f)
            tasks = data[worker]
            for file in rejected_files:
                print('file', file, 'rejected')
                tasks[f'file{file}'][0] = 'reject'

            # проставить accept в остальных файлах
            for file in tasks:
                if tasks[file][0] == 'review':
                    tasks[file][0] = 'accept'
                    print(file, 'accepted')

            # сохранить статусы заданий
            data.setdefault(worker, tasks)
            with open(baza_task, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                print(worker, 'status saved')

    # если админ отвечает на сообщение юзера
    elif worker:
        print('adm reply')
        # отпр ответ юзеру и всем админам
        for i in [worker]+admins:
            await bot.send_message(chat_id=i, text=lex['msg_from_admin']+txt_for_worker+admin_response)


# админ просит обнулить юзера
@router.message(Access(admins), lambda x: x.text, lambda x: x.text.lower() == 'del')
async def adm_del(msg: Message, state: FSMContext):
    await msg.answer(text='Введи пароль')
    await state.set_state(FSM.password)


# бот спрашивает пароль
@router.message(Access(admins), StateFilter(FSM.password))
async def adm_passw(msg: Message, state: FSMContext):
    if msg.text == TKN[:4]:
        await msg.delete()
        await msg.answer(text='Введи id, который нужно стереть')
        await state.set_state(FSM.delete)
    else:
        await msg.answer(text='Неверный пароль')


# админ обнуляет юзера
@router.message(Access(admins), StateFilter(FSM.delete))
async def adm_deleted(msg: Message, bot: Bot, state: FSMContext):
    # worker = вытащить id из текста сообщения
    worker = id_from_text(msg.text.lower())

    # чтение бд
    with open(baza_task, 'r', encoding='utf-8') as f1, open(baza_info, 'r', encoding='utf-8') as f2:
        data_tsk = json.load(f1)
        data_inf = json.load(f2)

    # скинуть бекап и удалить данные
    await bot.send_document(chat_id=msg.from_user.id, document=FSInputFile(path=baza_task))
    await bot.send_document(chat_id=msg.from_user.id, document=FSInputFile(path=baza_info))
    try:
        del data_tsk[worker]
    except KeyError:
        pass
    else:
        log(logs, worker, 'tasks deleted')
        print(worker, 'tasks deleted')
    try:
        del data_inf[worker]
    except KeyError:
        pass
    else:
        log(logs, worker, 'info deleted')
        print(worker, 'info deleted')

    # сохранить изменения
    with open(baza_task, 'w', encoding='utf-8') as f1, open(baza_info, 'w', encoding='utf-8') as f2:
        json.dump(data_tsk, f1, indent=2, ensure_ascii=False)
        json.dump(data_inf, f2, indent=2, ensure_ascii=False)

    await msg.answer(lex['deleted'])
    await state.clear()


# админ что-то пишет
@router.message(Access(admins), F.content_type.in_({'text'}))
async def adm_msg(msg: Message, bot: Bot):
    user = str(msg.from_user.id)
    txt = msg.text

    if txt.startswith(TKN[:4]):
        # рассылка всем юзерам
        with open(baza_task, 'r', encoding='utf-8') as f1:
            data_tsk = json.load(f1)
        for i in data_tsk:
            try:
                await bot.send_message(chat_id=i, text=txt[4:], parse_mode='HTML')
                print('msg_sent', i)
            except:
                print('not_found', i)

    # админ запрашивает файл
    elif txt.lower() == 'send bd':
        await bot.send_document(chat_id=user, document=FSInputFile(path=baza_task))
    elif txt.lower() == 'send info':
        await bot.send_document(chat_id=user, document=FSInputFile(path=baza_info))
    elif txt.lower() == 'send logs':
        await bot.send_document(chat_id=user, document=FSInputFile(path=logs))
    elif txt.lower() == 'send all':
        await bot.send_document(chat_id=user, document=FSInputFile(path=baza_task))
        await bot.send_document(chat_id=user, document=FSInputFile(path=baza_info))
        await bot.send_document(chat_id=user, document=FSInputFile(path=logs))

    # принять все файлы по айди юзера
    elif txt.lower().startswith('accept id'):
        # worker = вытащить id из текста сообщения
        worker = id_from_text(txt)

        # принять все файлы
        await accept_user(TKN, bot, worker)
        log(logs, worker, 'admin_accept')
        await msg.answer(f'✅ Приняты файлы от id{worker}')

    # отпр тсв со всем что юзер скинул на данный момент
    elif txt.lower().startswith('send id'):
        # worker = вытащить id из текста сообщения
        worker = id_from_text(txt)

        # отправить tsv админу
        path = await get_tsv(TKN, bot, msg, worker)
        await bot.send_document(chat_id=msg.from_user.id, document=FSInputFile(path=path))
        log(logs, worker, 'adm get_tsv')

    # если это админ, то создать два задания для отладки
    elif txt.lower() == 'adm start':
        # чтение БД
        with open(baza_task, 'r', encoding='utf-8') as f:
            data_tsk = json.load(f)
        with open(baza_info, 'r', encoding='utf-8') as f:
            data_inf = json.load(f)

        print('adm start')
        await bot.send_message(text=f'Ты админ. Доступно 2 задания для отладки /next', chat_id=user)
        data_tsk[user] = {"file01": ['status', 'file'], "file02": ['status', 'file']}
        # сохранить новые данные
        with open(baza_task, 'w', encoding='utf-8') as f:
            json.dump(data_tsk, f, indent=2, ensure_ascii=False)

    else:
        await msg.answer('Куда ты пишешь? Ответь на сообщение с крестиком')


# админ что-то пишет
@router.message(Access(admins), F.content_type.in_({'text'}))
async def adm_txt(msg: Message, bot: Bot):
    await msg.answer('Куда ты пишешь? Ответь на сообщение с крестиком')

