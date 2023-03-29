"""
    This module is designed for inline-keyboards that may occur frequently
"""


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def confirm_ikeyboard() -> InlineKeyboardMarkup:
    confirm = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data='yes'),
            InlineKeyboardButton(text="❌", callback_data="no")
        ]
    ])

    return confirm
