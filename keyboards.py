from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_kb() -> ReplyKeyboardMarkup:

    keyboard = [
        [KeyboardButton(text='Создать анкету')],
                ]

    kb = ReplyKeyboardMarkup(keyboard=keyboard,
                             resize_keyboard=True)

    return kb