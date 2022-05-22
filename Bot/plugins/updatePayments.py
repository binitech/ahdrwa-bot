from aiogram import types
from aiogram.dispatcher.filters import Text

from Bot import bot, dp, db


@dp.channel_post_handler(chat_type=types.ChatType.CHANNEL, chat_id=-1001337415083)
async def handle_from_chat(message: types.Message):
    message_text = message.text
    print(message)
    message_from = message_text.split("From: ")[1].split("\nDevice: ")[0]
    if message_from == "127":
        transaction_id = message_text.split("Your transaction number is\n")[1].split(". Your current ")[0]
        pay_amount = int(float(message_text.split("You have received ETB ")[1].split(" from ")[0]))
        pay_from = message_text.split(" from ")[1].split("  on ")[0]
        pay_time = message_text.split("  on ")[1].split(". Your transaction")[0]
        data = {
            "transaction_id": transaction_id,
            "pay_amount": pay_amount,
            "pay_from": pay_from,
            "pay_time": pay_time,
            "active": True
            }
        db.child("telebirr").update({transaction_id: data})
    elif message_from == "CBE Birr":
        transaction_id = message_text.split("Txn ID ")[1].split(".Your CBE Birr")[0]
        pay_amount = message_text.split(", you received ")[1].split("Br. from ")[0]
        pay_from = message_text.split(". from ")[1].split(" on ")[0]
        pay_time = message_text.split(" on ")[1].split(",Txn ID ")[0]
        data = {
            "transaction_id": transaction_id,
            "pay_amount": pay_amount,
            "pay_from": pay_from,
            "pay_time": pay_time,
            "active": True
        }
        db.child("cbebirr").update({transaction_id: data})
        print(transaction_id, pay_amount, pay_time, pay_from)
