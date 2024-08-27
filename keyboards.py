from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)



inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='', callback_data='')],
    [InlineKeyboardButton(text='', callback_data='')
     ]])

reply= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=''),KeyboardButton(text='')]])