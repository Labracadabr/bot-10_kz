import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from config import Config, load_config
import handler_admin
import handler_user
import handler_pd


async def main():
    # Инициализация
    config: Config = load_config()
    storage: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher(storage=storage)

    # Регистрируем роутеры в диспетчере
    dp.include_router(handler_pd.router)
    dp.include_router(handler_user.router)
    dp.include_router(handler_admin.router)
    # import handler_test
    # dp.include_router(handler_test.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=False)  # False > бот ответит на апдейты, присланные за время откл
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())