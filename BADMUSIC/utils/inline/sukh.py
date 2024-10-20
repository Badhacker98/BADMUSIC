from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def first_page(_):
    controll_button = [
        InlineKeyboardButton(text="๏ ᴍᴇɴᴜ ๏", callback_data=f"settingsback_helper"),
        InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"dilXaditi"),
    ]
    first_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="helpcallback hb1"),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="helpcallback hb2"),
                InlineKeyboardButton(text=_["H_B_3"], callback_data="helpcallback hb3"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_4"], callback_data="helpcallback hb4"),
                InlineKeyboardButton(
                    text=_["H_B_12"], callback_data="helpcallback hb12"
                ),
                InlineKeyboardButton(text=_["H_B_5"], callback_data="helpcallback hb5"),
            ],
            [
                InlineKeyboardButton(text=_["H_B_6"], callback_data="helpcallback hb6"),
                InlineKeyboardButton(
                    text=_["H_B_10"], callback_data="helpcallback hb10"
                ),
            ],
            [
                InlineKeyboardButton(text=_["H_B_8"], callback_data="helpcallback hb8"),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="helpcallback hb9"),
            ],
            [InlineKeyboardButton(text=_["H_B_11"], callback_data="helpcallback hb11")],
            controll_button,
        ]
    )
    return first_page_menu

