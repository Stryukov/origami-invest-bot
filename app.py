import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers.user_private import user_private_router
from app.handlers.user_group import user_group_router

from app.common.cmds import private


ALLOWED_UPDATES = ['message, edited_message']


load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
bot = Bot(
    token=os.getenv('TG_TOKEN', 'some_token'),
    parse_mode=ParseMode.HTML
)
dp = Dispatcher()
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    logger.info("Starting bot")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(
        commands=private, scope=types.BotCommandScopeAllPrivateChats()
    )
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
