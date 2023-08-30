from aiogram import types


RU = {
    "start": "Здравствуйте! Это Оригами-бот, я помогу вам сориентироваться по всем вопросам, связанным с нашей деятельностью.",
    "contact": "Читайте нас на канале: @origami_invest \nПишите нам: origami_invest@mail.ru",
    "back": "↩️ Вернуться назад",
    "form": "Заполнить анкету",
    "social": "Наши соцсети и контакты",
    "review_button": "Отправить отзыв/предложение",
    "first_button": "Часто задаваемые вопросы",
    "first_answer": "<b>💬 Как инвестировать?</b>\n \
К сожалению, мы пока не набираем инвесторов. Но обязательно будем выкладывать в своих соцсетях объявления обо всех изменениях.\n\n \
<b>💬 Хочу разместить свой товар в ваших проектах или хочу сотрудничать в соцсетях.</b>\n \
Напишите нам пожалуйста на <code>origami_invest@mail.ru</code> своё предложение и мы свяжемся с вами.\n\n \
<b>💬 Хоумстейджинг или ремонт для себя</b> \n \
Заполните пожалуйста анкету, мы свяжемся с вами.",
    "second_button": "Хочу оставить отзыв",
    "second_answer": "Напишите свой отзыв или предложения по улучшению качества наших услуг текстом в сообщении. \n\nНе забудьте оставить контакт, если вам нужна обратная связь.",
    "third_button": "Отправить анкету на ремонт и хоумстейджинг",
    "third_answer": "тут либо отдаю анкету, либо, если она не большая, то можно все вопросы поэтапно собрать ботом и отправить",
    "thanx": "Спасибо за ваш отзыв/предложение.",
}

BUTTONS = [
    types.InlineKeyboardButton(
            text=RU['first_button'],
            callback_data="first_button",
        ),
    types.InlineKeyboardButton(
            text=RU['second_button'],
            callback_data="second_button",
        ),
    types.InlineKeyboardButton(
            text=RU['third_button'],
            callback_data="third_button",
        )
]

BACK_BUTTON = [
    types.InlineKeyboardButton(
            text=RU['back'],
            callback_data="welcome",
        )
]

FORM_BUTTON = [
    types.InlineKeyboardButton(
            text=RU['form'],
            callback_data="request_form",
        )
]

SOCIAL_BUTTON = [
    types.InlineKeyboardButton(
            text=RU['social'],
            callback_data="social",
        )
]

REVIEW_BUTTON = [
    types.InlineKeyboardButton(
            text=RU['review_button'],
            callback_data="review",
        )
]
