from aiogram import types, Router
from aiogram.filters import CommandStart

from app.filters.chat_types import ChatTypeFilter
from app.kbs import reply

from misc.texts import RU

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(RU["start"], reply_markup=reply.start_kb)
