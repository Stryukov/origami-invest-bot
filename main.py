import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app.handlers.common import register_handlers_common


load_dotenv()
logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="🚀 (пере)запустить бота"),
        BotCommand(command="/contact", description="👤 наши контакты"),
        BotCommand(
            command="/cancel",
            description="🛑 отменить текущее действие"
        )
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")
    bot = Bot(token=os.getenv('TG_TOKEN', 'some_token'))
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_handlers_common(dp)
    await set_commands(bot)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
