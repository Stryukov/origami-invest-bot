from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text, IDFilter
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from dataclasses import dataclass

from misc.texts import RU, BUTTONS, BACK_BUTTON, FORM_BUTTON, \
    SOCIAL_BUTTON, REVIEW_BUTTON


@dataclass
class User:
    user_id: int
    uname: str
    fullname: str
    is_bot: bool
    locale: str


class Review(StatesGroup):
    waiting = State()


async def cmd_start(message: types.Message):
    await welcome_text(message)


async def cmd_contact(message: types.Message):
    await message.answer(RU['contact'])


async def call_contact(call: types.CallbackQuery):
    await cmd_contact(call.message)
    await call.answer()


async def welcome_text(message: types.Message):
    # нужно собрать информацию о пользователе и положить в БД
    # user = get_user_info(message)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*BUTTONS)
    await message.answer(RU['start'], reply_markup=keyboard)


async def begin(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await welcome_text(call.message)
    await call.message.delete()
    await call.answer()


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")
    await welcome_text(message)


def get_user_info(message: types.Message):
    return User(
        user_id=message.from_user.id,
        uname=message.from_user.username,
        fullname=message.from_user.full_name,
        is_bot=message.from_user.is_bot,
        locale=message.from_user.locale
    )


async def first_button(call: types.CallbackQuery):
    await show_msg(call, RU['first_answer'], (FORM_BUTTON + SOCIAL_BUTTON + BACK_BUTTON))


async def second_button(call: types.CallbackQuery):
    await Review.waiting.set()
    await show_msg(call, RU['second_answer'], (BACK_BUTTON))


async def third_button(call: types.CallbackQuery):
    await show_msg(call, RU['third_answer'], (FORM_BUTTON + BACK_BUTTON))


async def show_msg(call: types.CallbackQuery, text, buttons):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.answer(
        text,
        parse_mode=types.ParseMode.HTML,
        reply_markup=keyboard
    )
    await call.message.delete()
    await call.answer()


async def get_review(message: types.Message, state: FSMContext):
    # send review
    await message.answer(RU['thanx'])
    await state.finish()
    await welcome_text(message)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_contact, commands="contact", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(
        cmd_cancel, Text(equals="отмена", ignore_case=True), state="*"
    )
    dp.register_callback_query_handler(
        first_button, Text(startswith="first_button"), state="*"
    )
    dp.register_callback_query_handler(
        second_button, Text(startswith="second_button"), state="*"
    )
    dp.register_callback_query_handler(
        third_button, Text(startswith="third_button"), state="*"
    )
    dp.register_callback_query_handler(
        begin, Text(startswith="welcome"), state="*"
    )
    dp.register_callback_query_handler(
        call_contact, Text(startswith="social"), state="*"
    )
    dp.register_message_handler(get_review, state=Review.waiting)
