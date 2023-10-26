import os

dima = "992863889"
ilya = "899038082"
kris = "2137731767"
liza = '677214436'
anya = '639770334'
kate = ''

# Список id админов. Файлы приходят только первому по списку
# admins: list[str] = [anya]
# admins: list[str] = [ilya]
admins: list[str] = [anya, dima]

# Список id валидаторов. Можно вписать либо ничего, либо одного, либо двух - тогда одному будут идти четные, второму нечет
# Им приходят файлы и кнопки, доступны команды валидации
validators: list[str] = []

# сколько в боте заданий
total_tasks: int = 278

# где хранятся данные. тк я не умею в sql, то это просто json
baza_task = 'user_status.json'
baza_info = 'user_info.json'
logs = 'logs.json'
tasks_tsv = 'tasks.tsv'

# каналы сбора
referrals: tuple = ('smeight', 'gulnara', 'its_dmitrii', 'Natali', 'TD', 'Marina', 'schura', 'hanna', 'toloka', 'cat', 'airplane', 'one_more', 'good')
# https://t.me/TdTasksBot?start=...

# канал для логов
log_channel_id = '-1001642041865'

# # игнорить ли сообщения, присланные во время отключения бота
# ignor: bool = False

# проверить все ли ок
file_list = [baza_task, baza_info, logs, tasks_tsv]
for file in file_list:
    if not os.path.isfile(file):
        print('Ошибка! Файл не найден:', file)
        raise Exception
with open(tasks_tsv, 'r', encoding='utf-8') as f:
    task_list = f.readlines()
    if not len(task_list) == total_tasks:
        print('Ошибка! Неверное число заданий')
        raise Exception
