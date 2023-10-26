dima = "992863889"
ilya = "899038082"
kris = "2137731767"
liza = '677214436'
anya = '639770334'

# Список id админов. Файлы приходят только первому по списку
# admins: list[str] = [anya]
# admins: list[str] = [ilya]
admins: list[str] = [anya, dima]

# Список id валидаторов. Можно вписать либо ноль, либо одного, либо двух - тогда одному будут идти четные, второму нечет
# Им приходят файлы и кнопки, доступны команды валидации
validators: list[str] = ['']

# сколько в боте заданий
total_tasks: int = 27

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

#
