from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_rnd1 = KeyboardButton('/yn')
#go_btn_rnd1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_rnd1)
btn_rnd2 = KeyboardButton('/rnd')
go_btn_rnd1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_rnd1,btn_rnd2)