from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text, IDFilter
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    uname: str
    fullname: str
    is_bot: bool
    locale: str


async def cmd_start(message: types.Message):
    await welcome_text(message)


async def welcome_text(message: types.Message):
    user = get_user_info(message)
    await message.answer(f'Привет {user.uname}')


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


def get_user_info(message: types.Message):
    return User(
        user_id=message.from_user.id,
        uname=message.from_user.username,
        fullname=message.from_user.full_name,
        is_bot=message.from_user.is_bot,
        locale=message.from_user.locale
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
