from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def sub_button(unique_id, sub_type):
    main = InlineKeyboardMarkup(2)
    if sub_type == 'standard':
        main.add(
            InlineKeyboardButton("⚜ Premium ⚜️", callback_data=f"subscription_premium_{unique_id}"),
            InlineKeyboardButton("🔱 Platinum 🔱", callback_data=f"subscription_platinum_{unique_id}")
        )
    elif sub_type == 'premium':
        main.add(
            InlineKeyboardButton("🔱 Platinum 🔱", callback_data=f"subscription_platinum_{unique_id}")
        )
    else:
        main.add(
            InlineKeyboardButton("🔱 YOU ARE OUR TOP USER 🔱", callback_data=f"subscription_top")
        )
    return main


def pay_cancel(unique_id, sub_type):
    main = InlineKeyboardMarkup(2)
    main.add(
        InlineKeyboardButton("Proceed to Checkout", callback_data=f"checkout_{unique_id}_{sub_type}"),
        InlineKeyboardButton("Cancel", callback_data="cancel")
    )
    return main


def payments(unique_id, sub_type):
    main = InlineKeyboardMarkup(1)
    main.add(
        # InlineKeyboardButton("Mobile Card", callback_data=f"payment_card_{unique_id}_{sub_type}"),
        InlineKeyboardButton("TeleBirr", callback_data=f"payment_telebirr_{unique_id}_{sub_type}"),
        InlineKeyboardButton("CBE Birr", callback_data=f"payment_cbebirr_{unique_id}_{sub_type}"),
        InlineKeyboardButton("⬅️ Back", callback_data=f"subscription_{sub_type}_{unique_id}")
    )
    return main


def verify(pay_type, unique_id, sub_type):
    main = InlineKeyboardMarkup(2)
    main.add(
        InlineKeyboardButton("Verify Payment ♻️", callback_data=f"verify_{pay_type}_{unique_id}_{sub_type}"),
        InlineKeyboardButton("⬅️ Back", callback_data=f"checkout_{unique_id}_{sub_type}")
    )
    return main
