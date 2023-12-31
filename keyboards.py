from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


# privacy_en: str = "https://drive.google.com/file/d/1RddAFv77L6sL2tvPJBFxA5eI-Zb9Z1AC/view"
privacy_ru: str = "https://docs.google.com/document/d/1s9LkBxFPAuKnFxFWKcSNzXvMUG_2hSq7xehG8gZbKt4/edit"

# кнопки как опция ответа
# button_start = KeyboardButton(text='/start')
# button_help = KeyboardButton(text='/help')
button_next = KeyboardButton(text='/next')
button_stat = KeyboardButton(text='/status')

url_button = InlineKeyboardButton(text='Политика конфиденциальности', url=privacy_ru)
privacy_ok = InlineKeyboardButton(text='✅', callback_data='ok_pressed')

admin_ok: InlineKeyboardButton = InlineKeyboardButton(text='✅', callback_data='admin_ok')
admin_no: InlineKeyboardButton = InlineKeyboardButton(text='❌', callback_data='admin_no')

# клавиатуры из таких кнопок
keyboard_privacy = InlineKeyboardMarkup(inline_keyboard=[[url_button]])
keyboard_ok = InlineKeyboardMarkup(inline_keyboard=[[privacy_ok]])
keyboard_admin = InlineKeyboardMarkup(inline_keyboard=[[admin_ok], [admin_no]])
keyboard_user = ReplyKeyboardMarkup(keyboard=[[button_next], [button_stat]], resize_keyboard=True)
