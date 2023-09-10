from aiogram import types


RU = {
    "start": "Здравствуйте! Это Оригами-бот, я помогу вам сориентироваться по всем вопросам, связанным с нашей деятельностью.",
    "contact": "Мы в телеграме: @origami_invest \nМы в инстаграме: https://www.instagram.com/origami_invest \nПишите нам: origami_invest@mail.ru",
    "back": "↩️ Вернуться назад",
    "form": "Заполнить анкету",
    "social": "Наши соцсети и контакты",
    "review_button": "Отправить отзыв/предложение",
    "first_button": "Часто задаваемые вопросы",
    "first_answer": "<b>💬 Как инвестировать?</b>\n \
К сожалению, мы пока не набираем инвесторов. Но обязательно будем выкладывать в своих соцсетях объявления обо всех изменениях.\n\n \
<b>💬 Хочу разместить свой товар в ваших проектах или хочу сотрудничать в соцсетях.</b>\n \
Напишите нам пожалуйста на <code>origami_invest@mail.ru</code> своё предложение и мы свяжемся с вами.\n\n \
<b>💬 Хоумстейджинг</b> \n \
Заполните пожалуйста анкету, мы свяжемся с вами.",
    "second_button": "Хочу оставить отзыв",
    "second_answer": "Напишите свой отзыв или предложения по улучшению качества наших услуг текстом в сообщении. \n\nНе забудьте оставить контакт, если вам нужна обратная связь.",
    "third_button": "Отправить анкету на ремонт и хоумстейджинг",
    "third_answer": "Заполните, пожалуйста, нашу анкету и мы свяжемся с вами в самое ближайшее время.",
    "thanx": "Спасибо за ваш отзыв/предложение.",
    "err_send_msg": "⛔️ Ошибка отправки отзыва/предложения. Попробуйте отправить позднее.",
    "admin_notify": "⛔️ Ошибка отправки отзыва: \n\n",
    "text_review": "\n\nТекст отзыва:",

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
            url='https://forms.gle/8Lu2a9Pt7YgGZq8o9',
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
