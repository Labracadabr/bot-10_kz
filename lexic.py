from settings import mngr

# RU: dict[str, dict[str, str]] = {}
lex: dict = {
        # admin
        'adm_review': 'Принять ВСЕ файлы от',
        'msg_to_admin': 'Сообщение от',
        'msg_from_admin': 'Сообщение от администратора:',
        'deleted': 'Удалено, вот бекап до удаления',
        'wrong_rej_form': 'Неверный формат: каждая новая строка должна начинаться с числа и '
                          'оканчиваться переносом строки.\nНапиши причину отказа снова.',
        # users
        'help': f'Если что-то не работает, нажмите /start или /next или напишите {mngr}',

        'cancel': 'Укажите через пробел номера заданий (две цифры), для которых вы хотите отменить отправку файла. Пример сообщения:'
                  '\n\n01 02 16',
        'cancel_fail': 'Нет файлов, которые вы можете удалить',
        'cancel_ok': 'Ок. Удалены ваши файлы из заданий: ',
        'cancel_not_found': 'Задания под следующими номерами либо уже отправлены на проверку, либо вы их не присылали: ',
        'cancel_wrong_form': 'Неверный формат. Я ожидаю номера заданий через пробел.',

        'no_ref': 'Ссылка недействительна. Спросите ссылку у того, кто привел вас к нам.',
        'start': 'Привет!\n\n'
                 'Мы собираем фото и видео для <b>обучения нейросети</b> распознавать эмоции, жесты и прочие действия.\n\n'
                 'Вам предстоит выполнить 65 заданий. В каждом будет дан пример в виде ссылки на файл из Гугл-диска и краткое описание, '
                 'что нужно заснять (<a href="https://drive.google.com/drive/folders/1izl1XW_behpwcF3TQs8yTRTcok9Og_WT">тут папка</a> со всеми заданиями, '
                 'далее вы будете получать по порядку, по одному). '
                 'Когда вы выполните все 65 заданий - ваши файлы будут отправлены нам <b>на проверку</b>.\n\n'
                 'Если задание будет выполнено не правильно - мы его отклоним и оно будет вам доступно для повторного выполнения. '
                 'Когда все 65 заданий будут успешно приняты - вы получите уведомление, мы проверим вашу работу и после этого в течение недели вы получите <b>оплату</b>.\n'
                 '\nМожете нажать:'
                 '\n/next для выдачи следующего задания'
                 '\n/status для просмотра статуса ваших заданий'
                 '\n/help чтобы сообщить о проблемах с ботом'
                 '\n/cancel чтобы отменить отправку файла.'
                 '\n\nДля выполнения задания приготовьте: Большие наушники (либо головной убор), две пары очков (с прозрачными линзами и солнцезащитные), '
                 'два телефона, бутылка воды, еда, письменная ручка, медицинская маска.'
                 '\n\nПрежде чем продолжить, пожалуйста, ознакомьтесь с нашей <b>политикой конфиденциальности</b> и нажмите кнопку ✅.',

        'start_again': 'Вы уже числитесь в базе данных, можете продолжать задания: /next',
        'ban': 'Вам заблокирован доступ к заданиям.',
        'privacy_missing': 'Нажмите галочку, чтобы согласиться с политикой конфиденциальности.',
        'instruct1': 'Ознакомьтесь с <b>требованиями</b> к отправляемым файлам:\n\n'
                     '- Убедитесь, что объектив вашей камеры чист\n'
                     '- <b>Телефон должен стоять</b> на столе, чтобы избежать тряски видео\n'
                     '- Каждое видео должно длиться от 5 секунд\n'
                     '- Нельзя прикрывать никакую часть лица, даже своими пальцами (если иное не показано в примере)\n'
                     '- Лицо должно быть хорошо видно, на свету, не обрезано\n'
                     '- Все видео и фото обязательно должны быть <b>ГОРИЗОНТАЛЬНЫЕ</b> (как в примерах)\n'
                     '- Выполняйте задания точь в точь, как в примере (Если в примере человек поворачивает голову '
                     'в свое лево, то вы поворачиваете также в <b>свое лево</b>)\n'
                     '- Если в примере меняется задний фон и одежда, то вам требуется сделать то же самое\n'
                     '\n Отдельные требования к <b>фону и одежде</b>:\n'
                     '- На все задания у вас должно быть всего должно быть два разных сочетания фона и одежды.\n'
                     '- На фоне должны быть элементы интерьера (не монотонная стена)\n'
                     '- В каждом задании мы укажем, какой из двух фонов нужно использовать (это также видно в примерах к заданиям)\n',

        'full_hd': 'Нужно отправить файл <b>без сжатия</b>. Если не знаете как, то'
                   ' <a href="https://www.youtube.com/embed/qOOMNJ0gIss">посмотрите пример</a> (9 сек).',
        'instruct2': 'Можете приступать к выполнению - нажмите команду /next для получения следующего задания. ',

        'album': 'Отправляйте файлы по одному, не группой',
        'receive': 'Получен файл для задания {}.\nНажмите /next для следующего задания',

        'all_sent': 'Спасибо! Вы отправили все нужные файлы. Ожидайте проверки вашей работы.\n'
                    'Нажмите команду /personal, чтобы указать ваш пол и возраст, если еще не указывали.',
        'no_more': 'Нет доступных заданий',
        'reject': 'Мы проверили вашу работу. К сожалению, часть файлов не прошла проверку. Ознакомьтесь с нашими '
                  'комментариями и нажмите команду /next для получения задания.',
        'all_approved': 'Ура! Ваш сет успешно прошел первую проверку на качество.\n'
                        'В течение недели мы более внимательно проверим вашу работу. Возможно, потребуется внести новые исправления. '
                        'Если всё сделано правильно, то с вами свяжется человек, от которого вы получили приглашение. Ваш айди: ',

        # персуха
        'age': 'Укажите ваш возраст - две цифры слитно',
        'age_bad': 'Неверный формат, я ожидаю две цифры',
        'gender': 'Укажите ваш пол. Отправьте одну латинскую букву: m (мужской) или f (женский)',
        'gender_bad': 'Неверный формат, я ожидаю одну латинскую букву: m или f',
        'fio': 'Укажите ваше ФИО',
        'fio_bad': 'Неверный формат, я ожидаю два или три слова',
        'pd_ok': 'Ваши данные сохранены.',

        # шаблоны
        'user_pd':     {
                  "referral": None,
                  "first_start": None,
                  "accept_date": None,
                  "age": None,
                  "gender": None,
                  "tg_username": None,
                  "tg_fullname": None,
                  "tasks": None,
                  "last_sent": None,
                  "fio": None,
                  "status": None
                },
        'user_account': {
                        "file01": ['status', 'file'],
            "file02": ['status', 'file'],
            "file03": ['status', 'file'],
            "file04": ['status', 'file'],
            "file05": ['status', 'file'],
            "file06": ['status', 'file'],
            "file07": ['status', 'file'],
            "file08": ['status', 'file'],
            "file09": ['status', 'file'],
            "file10": ['status', 'file'],
            "file11": ['status', 'file'],
            "file12": ['status', 'file'],
            "file13": ['status', 'file'],
            "file14": ['status', 'file'],
            "file15": ['status', 'file'],
            "file16": ['status', 'file'],
            "file17": ['status', 'file'],
            "file18": ['status', 'file'],
            "file19": ['status', 'file'],
            "file20": ['status', 'file'],
            "file21": ['status', 'file'],
            "file22": ['status', 'file'],
            "file23": ['status', 'file'],
            "file24": ['status', 'file'],
            "file25": ['status', 'file'],
            "file26": ['status', 'file'],
            "file27": ['status', 'file'],
            "file28": ['status', 'file'],
            "file29": ['status', 'file'],
            "file30": ['status', 'file'],
            "file31": ['status', 'file'],
            "file32": ['status', 'file'],
            "file33": ['status', 'file'],
            "file34": ['status', 'file'],
            "file35": ['status', 'file'],
            "file36": ['status', 'file'],
            "file37": ['status', 'file'],
            "file38": ['status', 'file'],
            "file39": ['status', 'file'],
            "file40": ['status', 'file'],
            "file41": ['status', 'file'],
            "file42": ['status', 'file'],
            "file43": ['status', 'file'],
            "file44": ['status', 'file'],
            "file45": ['status', 'file'],
            "file46": ['status', 'file'],
            "file47": ['status', 'file'],
            "file48": ['status', 'file'],
            "file49": ['status', 'file'],
            "file50": ['status', 'file'],
            "file51": ['status', 'file'],
            "file52": ['status', 'file'],
            "file53": ['status', 'file'],
            "file54": ['status', 'file'],
            "file55": ['status', 'file'],
            "file56": ['status', 'file'],
            "file57": ['status', 'file'],
            "file58": ['status', 'file'],
            "file59": ['status', 'file'],
            "file60": ['status', 'file'],
            "file61": ['status', 'file'],
            "file62": ['status', 'file'],
            "file63": ['status', 'file'],
            "file64": ['status', 'file'],
            "file65": ['status', 'file']
                      },

        # задания
        'tasks': {
            # Behavior:
            'file01': '<a href="https://drive.google.com/file/d/14bYM2Y_N4SFLIXsyJ6fpLPWX1MSh7Zqd/view?usp=drive_link">Задание 01, Фон № 1:</a> Drink	(Для записи видео потребуется бутылка воды) Снимите как вы пьете воду из бутылки. Откройте бутылку, попейте немного напитка, закройте бутылку.',
            'file02': '<a href="https://drive.google.com/file/d/19L-ac1bbe6kh7cgxiDyUO8MET7VX6Jpk/view?usp=drive_link">Задание 02, Фон № 1:</a> Eat-food	(Требуется что-то из еды, по типу снэка без упаковки) Снимите как вы едите что-то, например, любой снэк, и проглотите.',
            'file03': '<a href="https://drive.google.com/file/d/1D9XJL0fS9nZ4OqQ-D_Csgr6dnk5Kf-ol/view?usp=drive_link">Задание 03, Фон № 1:</a> Play-phone	(Для записи видео потребуется второй телефон) Снимите как вы печатаете на телефоне, пальцы должны быть видны, а взгляд направлен в телефон.',
            'file04': '<a href="https://drive.google.com/file/d/1mtSy2ShtvrTmAtOpEINJeTdYhLDlgdz9/view?usp=drive_link">Задание 04, Фон № 1:</a> Turn-pen	(Для записи видео потребуется письменная ручка) Снимите как вы крутите ручку в левой руке, как это показано в примере.',
            'file05': '<a href="https://drive.google.com/file/d/1VZI4pQF6gd3szi1xmoDrwO5Sr80vgyB5/view?usp=drive_link">Задание 05, Фон № 2:</a> Body-forth-back	Снимите как вы наклоняйте тело вперед-назад-вперед-назад, как это показано в примере.',
            'file06': '<a href="https://drive.google.com/file/d/1lmgJm0muj2fJZ1YaVpxBsgAx801Kxiae/view?usp=drive_link">Задание 06, Фон № 2:</a> Body-left-right	Снимите как вы наклоняйте тело вместе с головой сначала влево, после вправо, как это сделано в примере. ',
            'file07': '<a href="https://drive.google.com/file/d/1tpcY-LKjf5EMOw6Aao5iuSEZxQNMPBaB/view?usp=drive_link">Задание 07, Фон № 2:</a> Body-rotate	Снимите как вы поворачивайте тело вместе с головой влево-вправо (голова смотрит прямо, как в примере).',
            'file08': '<a href="https://drive.google.com/file/d/14gxs3K9uiUr2CWIJ_QTzuoINpcahAhWA/view?usp=drive_link">Задание 08, Фон № 2:</a> Fold-arm	Снимите как вы складывайте руки на груди, а после выпрямляйте их в обычное положение.',
            'file09': '<a href="https://drive.google.com/file/d/1DhUO-2aq-VD3-RI8zYHdicbQBBHF5qmw/view?usp=drive_link">Задание 09, Фон № 2:</a> Shrug-shoulder	Снимите как вы пожимаете плечами вверх-вниз, как будто говорите “не знаю”, как показано в примере.',
            'file10': '<a href="https://drive.google.com/file/d/10bRmPqkIOGUlmMlCag3mu9olMVzrNJJj/view?usp=drive_link">Задание 10, Фон № 2:</a> Stretch-arm	Снимите как вы тянитесь, нужно поднять руки и завести их за спину, чтобы это выглядело по-настоящему, как в примере.',
            'file11': '<a href="https://drive.google.com/file/d/1nfVGka8x-LnMxLXDKqnVA2szfO8_htB7/view?usp=drive_link">Задание 11, Фон № 2:</a> Up-down	Снимите как вы встаете и садитесь.',
            'file12': '<a href="https://drive.google.com/file/d/1D9Shqnc-GT4pRvIn7YtCh_JD1or2tn9u/view?usp=drive_link">Задание 12, Фон № 1:</a> Amazed	(В этом видео важна эмоция) Снимите ваше удивление идентично примеру.',
            'file13': '<a href="https://drive.google.com/file/d/1Asg0zzVXKCTvBGi49qg8t51HWKTnrVi3/view?usp=drive_link">Задание 13, Фон № 1:</a> Anger	(В этом видео важна эмоция) Снимите как вы злитесь идентично примеру.',
            'file14': '<a href="https://drive.google.com/file/d/1FtHT22RWF8QYwLfRTAT_PXYhVUPuGygO/view?usp=drive_link">Задание 14, Фон № 1:</a> Disgusted	(В этом видео важна эмоция) Снимите вашу эмоцию отвращения идентично примеру.',
            'file15': '<a href="https://drive.google.com/file/d/1zjPBk8CD8hyO7iOsS6FPgh6OATp5AtIT/view?usp=drive_link">Задание 15, Фон № 1:</a> Happy	(В этом видео важна эмоция) Снимите эмоцию счастья идентично примеру.',
            'file16': '<a href="https://drive.google.com/file/d/1rfjchs4I_EAROFdOSeRvhovlZFpAJN6i/view?usp=drive_link">Задание 16, Фон № 1:</a> Normal	(В этом видео важна эмоция) Снимите ваше обычное лицо идентично примеру.',
            'file17': '<a href="https://drive.google.com/file/d/1aIlIanjEzkIBA0TyeOv7aHr1OxToBlEq/view?usp=drive_link">Задание 17, Фон № 1:</a> Sad	(В этом видео важна эмоция) Снимите эмоцию грусти идентично примеру.',
            'file18': '<a href="https://drive.google.com/file/d/1EZqQZCf1Qeq8dHgLOJYJLGUUHazJLLep/view?usp=drive_link">Задание 18, Фон № 1:</a> Scared	(В этом видео важна эмоция) Снимите как вы испугались идентично примеру.',
            'file19': '<a href="https://drive.google.com/file/d/1IZtDmoNUsYL0N4PF3Ob-c9kjASEQnr8F/view?usp=drive_link">Задание 19, Фон № 1:</a> Deep-breath	Снимите ваш глубокий вдох. При этом нужно надуть щеки и полностью выдохнуть.',
            'file20': '<a href="https://drive.google.com/file/d/1BC4hbSFc5_ijQjhpX_3f1y8E0KOXSRNU/view?usp=drive_link">Задание 20, Фон № 1:</a> Eye-closed	Снимите как вы зажмуриваетесь, а потом откройте глаза.',
            'file21': '<a href="https://drive.google.com/file/d/17mOicp3XE2VU8dioQiwPGzSpkBClKQTN/view?usp=drive_link">Задание 21, Фон № 1:</a> Eye-roll	Повторите движение зрачков в этом видео. Нужно сначала посмотреть зрачками вверх, затем медленно переместить их вправо.',
            'file22': '<a href="https://drive.google.com/file/d/161g32put2RKzyqRvTL1CMj5YdKy2uuVZ/view?usp=drive_link">Задание 22, Фон № 1:</a> Eye-stare	Поднимите брови и широко откройте глаза, затем вернитесь в обычное положение лица.',
            'file23': '<a href="https://drive.google.com/file/d/141HNzEVt3ACcu48bIWUHALD7GNfcFMU2/view?usp=drive_link">Задание 23, Фон № 1:</a> Mouth-open	Откройте широко рот, затем медленно закройте. ',
            'file24': '<a href="https://drive.google.com/file/d/1yA-FAUAFVaAHOxhh0DSSvt5Fvw8yirb5/view?usp=drive_link">Задание 24, Фон № 1:</a> Mouth-pout	Сделайте губы трубочкой, затем вернитесь в обычное положение лица.',
            'file25': '<a href="https://drive.google.com/file/d/1laBs74n9RdwIwFksIYYdiv80uubIBBmB/view?usp=drive_link">Задание 25, Фон № 1:</a> Mouth-pucker	Втяните губы, как показано на видео.',
            'file26': '<a href="https://drive.google.com/file/d/1yXJrhYzs6UH8FnEEBpYmvbNrOYT6I9xs/view?usp=drive_link">Задание 26, Фон № 1:</a> Put-tongue	Откройте широко рот и покажите язык, затем закройте рот.',
            'file27': '<a href="https://drive.google.com/file/d/1Q-E8HOdpRsHnjRlhUkN6N9UNvz_Ed1Zt/view?usp=drive_link">Задание 27, Фон № 1:</a> Touch-chin	Потрогайте подбородок большим и указательным пальцами, как показано в примере.',
            'file28': '<a href="https://drive.google.com/file/d/13i8iOrT4nAqAape_g2LvpC8INX7_L9kB/view?usp=drive_link">Задание 28, Фон № 1:</a> Touch-ear	Потрогайте ухо большим и указательным пальцами, как показано в примере',
            'file29': '<a href="https://drive.google.com/file/d/1Amq1N1O_vZQC1fR5qfE_1_VoQLuZFkZs/view?usp=drive_link">Задание 29, Фон № 1:</a> Touch-eye	Потрогайте только один глаз двумя пальцами, как показано в примере.',
            'file30': '<a href="https://drive.google.com/file/d/1xEoSgXtJOsmAlDipk-0hGJPd6jfLN3O8/view?usp=drive_link">Задание 30, Фон № 1:</a> Touch-face	Потрогайте щеку всеми пальцами одной рукой, как показано в примере.',
            'file31': '<a href="https://drive.google.com/file/d/1vphpWl3O2K0J8lzIlTAWsv3rcJqGNi7Z/view?usp=drive_link">Задание 31, Фон № 1:</a> Touch-forehead	Потрогайте лоб ладонью, как показано в примере.',
            'file32': '<a href="https://drive.google.com/file/d/1OZ5x6HF3Crf-FADWkKt19HRGSg1CrAEj/view?usp=drive_link">Задание 32, Фон № 1:</a> Touch-glasses	Поправьте очки одной рукой за душку, как показано в примере.',
            'file33': '<a href="https://drive.google.com/file/d/1TLxipCoi29ZnM_PsSSvrBCRKXuszXeOq/view?usp=drive_link">Задание 33, Фон № 1:</a> Touch-head	Потрогайте волосы на голове ладонью руки, как показано в примере.',
            'file34': '<a href="https://drive.google.com/file/d/1YORFJWOuAMRz8LAXJKvvTU3SUXniYPsD/view?usp=drive_link">Задание 34, Фон № 1:</a> Touch-mouth	Потрогайте рот пальцами и ладонью, как показано в примере.',
            'file35': '<a href="https://drive.google.com/file/d/1G3WLi-A38mqZSD16QICrRYinGQBLlU4n/view?usp=drive_link">Задание 35, Фон № 1:</a> Touch-nose	Потрогайте нос большим и указательным пальцами, как показано в примере.',
            'file36': '<a href="https://drive.google.com/file/d/1ai02BmUv9tb1zrGLrkxqNje5A4b8kpG2/view?usp=drive_link">Задание 36, Фон № 1:</a> Glasses-headset	Сфотографируйтесь в очках и любых наушниках (Большие наушники, как в примере, или маленькие, но чтобы их было видно). В очках не должно быть бликов.',
            'file37': '<a href="https://drive.google.com/file/d/109Ckvdc2e6gTvHZpxw3WO64t88FOX5zr/view?usp=drive_link">Задание 37, Фон № 1:</a> Mask	Фото в медицинской маске',
            'file38': '<a href="https://drive.google.com/file/d/1VFdRjy6vbubYczeqmbX1bDGWQvo3uniO/view?usp=drive_link">Задание 38, Фон № 1:</a> Normal	Фото без эмоций, обычное лицо',
            'file39': '<a href="https://drive.google.com/file/d/1g33g1DQ6JlDz7ppiuIO6FwnorTO1mVbD/view?usp=drive_link">Задание 39, Фон № 1:</a> Sunglasses	Сделайте фотографию в солнцезащитных очках (темные очки).',
            'file40': '<a href="https://drive.google.com/file/d/1VXa_7KkyDBsvnifDuhBsZCyMeSW6C4WH/view?usp=drive_link">Задание 40, Фон № 1:</a> Clapping	Снимите как вы хлопаете в ладошки, не закрывая лицо руками.',
            'file41': '<a href="https://drive.google.com/file/d/1orqIiF4y7bfZRnHU9V52F00CIhkOgD-k/view?usp=drive_link">Задание 41, Фон № 1:</a> Greeting	Снимите как вы приветствуете кого-то, не закрывая лицо руками.',
            'file42': '<a href="https://drive.google.com/file/d/1j95rtx32sR-k635qCVq4pl_un10VpJ4b/view?usp=drive_link">Задание 42, Фон № 1:</a> Dislike	Фото: палец вниз',
            'file43': '<a href="https://drive.google.com/file/d/1R7fUaB8DevIl52yiJprWosayjMLKzdIa/view?usp=drive_link">Задание 43, Фон № 1:</a> Like	Фото: палец вверх',
            'file44': '<a href="https://drive.google.com/file/d/1Of1Joar-DqEjHNZ58-Q_5DE6-NHzm_fI/view?usp=drive_link">Задание 44, Фон № 1:</a> Make-a-fist	Фото: покажите кулак и держите руку на уровне головы (как в примере)',
            'file45': '<a href="https://drive.google.com/file/d/1M6CCnERhE_02D07M3dd8B4sTWGf9HkHq/view?usp=drive_link">Задание 45, Фон № 1:</a> Number-1	Фото: Показать пальцем цифру 1 (как в примере)',
            'file46': '<a href="https://drive.google.com/file/d/1k1BSpQb45BfMfjuTBHYhIioh62UZsZow/view?usp=drive_link">Задание 46, Фон № 1:</a> Number-2	Фото: Показать пальцами цифру 2 (как в примере)',
            'file47': '<a href="https://drive.google.com/file/d/1M_RVhMujraY08OYDglM0lr5w-oclzszc/view?usp=drive_link">Задание 47, Фон № 1:</a> Number-3	Фото: Показать пальцами цифру 3 (как в примере)',
            'file48': '<a href="https://drive.google.com/file/d/1lH8-zwAKICOfvGIhAOtzVKSQFYg8FHd_/view?usp=drive_link">Задание 48, Фон № 1:</a> Number-4	Фото: Показать пальцами цифру 4 (как в примере)',
            'file49': '<a href="https://drive.google.com/file/d/17mBYlZjIE1fXIbJCdqjpymTv5EwJG4Sd/view?usp=drive_link">Задание 49, Фон № 1:</a> Number-5	Фото: Показать пальцами цифру 5 (как в примере)',
            'file50': '<a href="https://drive.google.com/file/d/1HZviA2W_4RKgdzi3UQaFizUYFpHwAfvK/view?usp=drive_link">Задание 50, Фон № 1:</a> Number-6	Фото: Показать пальцами цифру 6 (как в примере)',
            'file51': '<a href="https://drive.google.com/file/d/1OElR2QqqC1iEqv5K5gNw8T48J5akRE-9/view?usp=drive_link">Задание 51, Фон № 1:</a> Number-8	Фото: Показать пальцами цифру 8 (как в примере), большой и указательный пальцы должны быть вытянуты',
            'file52': '<a href="https://drive.google.com/file/d/1fOKd-2pZPpuyIGanZf5Vwfbx1pjmCP-4/view?usp=drive_link">Задание 52, Фон № 1:</a> OK	Фото: жест "ok"',
            'file53': '<a href="https://drive.google.com/file/d/1l7N6QVmwVOVBGpdk2YOsF5VUSZHg7wVD/view?usp=drive_link">Задание 53, Фон № 1:</a> Point-finger	Фото: показать указательный палец, направленный на голову.',
            'file54': '<a href="https://drive.google.com/file/d/1sk1V_jj_0IHV4KBxLl5iboznhTauXKZ8/view?usp=drive_link">Задание 54, Фон № 1:</a> Put-palms-together	Фото: 🙏 Сложить ладони',
            'file55': '<a href="https://drive.google.com/file/d/1kKNAvIcxeX3yVCj92akhDNVQtB0A8DO4/view?usp=drive_link">Задание 55, Фон № 1:</a> Show-hand	Фото: повторите положение рук из примера',
            'file56': '<a href="https://drive.google.com/file/d/1YA3V-TigMn-CsXcHBSJlouIGLiz57UXi/view?usp=drive_link">Задание 56, Фон № 1:</a> Show-hand2	Фото: повторите положение рук из примера',
            'file57': '<a href="https://drive.google.com/file/d/1-HN39MozLHHBqrvOxMnjmNqsLbpbOxV2/view?usp=drive_link">Задание 57, Фон № 1:</a> Show-hand3	Фото: повторите положение рук из примера',
            'file58': '<a href="https://drive.google.com/file/d/1E_ipDr0KLPgB-Dv6nFgGGoXdDxp6KNiR/view?usp=drive_link">Задание 58, Фон № 1:</a> Single-hand-heart	Фото: 🫰🏻 "Тиктокерское сердце"',
            'file59': '<a href="https://drive.google.com/file/d/1S-xpUXldA0pHzvHeAwDQx21nscQXk_hK/view?usp=drive_link">Задание 59, Фон № 1:</a> Two-hand-heart	Фото: Сердце двумя руками',
            'file60': '<a href="https://drive.google.com/file/d/12vf2QVnhxs_gElqLkFPxKSw6xgiyCYgh/view?usp=drive_link">Задание 60, Фон № 2:</a> GlassesPitch	(Для записи потребуются очки) Снимите как вы отклоняете голову назад и наклоняете её вперед, не наклоняя при этом тело.',
            'file61': '<a href="https://drive.google.com/file/d/1c7cppQhpx74guNZZx9jxG54BTJPZUWNP/view?usp=drive_link">Задание 61, Фон № 2:</a> GlassesRoll	(Для записи потребуются очки) Снимите как вы наклоняете голову влево-вправою. Не надо наклонять тело, только голову.',
            'file62': '<a href="https://drive.google.com/file/d/11rjkofMR33oVXHzFGa7gTpJviCX5FX3h/view?usp=drive_link">Задание 62, Фон № 2:</a> GlassesYaw	(Для записи потребуются очки) Снимите как вы поворачиваете голову влево-вправо. Не надо поворачивать тело, только голову.',
            'file63': '<a href="https://drive.google.com/file/d/1D_JvBisheWLNipYnzuR-zkXH7X9XEXee/view?usp=drive_link">Задание 63, Фон № 2:</a> NoGlassesPitch	Снимите как вы отклоняете голову назад и наклоняете её вперед, не наклоняя при этом тело.',
            'file64': '<a href="https://drive.google.com/file/d/1PphVEamh4_hYfC1aTMWDIMjJM2UOIloF/view?usp=drive_link">Задание 64, Фон № 2:</a> NoGlassesRoll	Снимите как вы наклоняете голову влево-вправою. Не надо наклонять тело, только голову.',
            'file65': '<a href="https://drive.google.com/file/d/1uKVAxlC1Fhnmtnz8o-KR1Eh3djjAQLvV/view?usp=drive_link">Задание 65, Фон № 2:</a> NoGlassesYaw	Снимите как вы поворачиваете голову влево-вправо. Не надо поворачивать тело, только голову.',
            },
        'log': 'so-dev',

}
