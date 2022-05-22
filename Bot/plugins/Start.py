from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import config
from Bot.helpers import buttons
from Bot import dp, db
from aiogram import types
from requests import request
from Bot.helpers import states
from Bot.helpers import strings


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    await message.answer(strings.START_TEXT.format(message.from_user.first_name), parse_mode="HTML")
    await states.UserStatus.user_id.set()


@dp.message_handler(state=states.UserStatus.user_id)
async def id_state(message: types.Message, state: FSMContext):
    url = config.API_URL_USER
    user_id = message.text
    if len(user_id) != 24:
        await message.answer(strings.INVALID_TEXT)
        return
    response = (request("GET", url + user_id)).json()
    try:
        text = response['msg']
        await message.answer(strings.INVALID_TEXT)
        return
    except KeyError:
        TEXT = strings.STATUS_TEXT.format(response['username'], response['subscription'], response['registerd_date'])
        await message.answer_photo(
            config.USER_PROFILE,
            TEXT,
            reply_markup=buttons.sub_button(message.text, response['subscription']))
        async with state.proxy() as data:
            data['user_id'] = message.text
    await state.finish()


@dp.callback_query_handler(Text(startswith="subscription_"))
async def subscription_handler(query: types.InlineQuery):
    message = query.message
    if query.data == 'subscription_top':
        await query.answer("You are already subscribed to the top, you can\'t go more😁", show_alert=True)
        return
    unique_id = query.data.split("_")[-1]
    if query.data.startswith("subscription_premium"):
        await message.edit_caption(strings.PREMIUM_TEXT,
                                   reply_markup=buttons.pay_cancel(unique_id, "premium"),
                                   parse_mode="HTML")
    elif query.data.startswith("subscription_platinum"):
        await message.edit_caption(strings.PLATINUM_TEXT,
                                   reply_markup=buttons.pay_cancel(unique_id, "platinum"),
                                   parse_mode="HTML")


@dp.callback_query_handler(Text(startswith="checkout"))
async def checkout_handler(query: types.InlineQuery):
    message = query.message
    mains = query.data.split("_")
    await message.edit_caption(strings.PAYMENT_TEXT,
                               parse_mode="HTML",
                               reply_markup=buttons.payments(mains[1], mains[2]))


@dp.callback_query_handler(Text(startswith="payment"))
async def payment_handler(query: types.InlineQuery):
    mains = query.data.split("_")
    message = query.message
    print(mains)
    amount = 0
    if mains[3] == 'premium':
        amount = 10
    else:
        amount = 20
    if mains[1] == 'telebirr':
        await message.edit_caption(strings.TELEBIRR_PAY_TEXT.format(amount),
                                   parse_mode="HTML",
                                   reply_markup=buttons.verify(mains[1], mains[2], mains[3]))
    elif mains[1] == 'cbebirr':
        await message.edit_caption(strings.CBEBIRR_PAY_TEXT.format(amount),
                                   parse_mode="HTML",
                                   reply_markup=buttons.verify(mains[1], mains[2], mains[3]))


@dp.callback_query_handler(Text(startswith="verify"))
async def verify_handler(query: types.InlineQuery, state: FSMContext):
    message = query.message
    mains = query.data.split("_")
    async with state.proxy() as data:
        if mains[1] == "telebirr":
            data['payment_method'] = 'telebirr'
            await message.answer(strings.TELEBIRR_REF_TEXT)

        elif mains[1] == 'cbebirr':
            data['payment_method'] = 'cbebirr'
            await message.answer(strings.CBEBIRR_REF_TEXT)
        data['user_id'] = mains[2]
        data['sub_type'] = mains[3]
        await states.UserStatus.payment_id.set()


@dp.message_handler(state=states.UserStatus.payment_id)
async def verify_telebirr(message: types.Message, state: FSMContext):
    if message.text == '/cancel':
        await message.answer("Process canceled.")
        await state.finish()
        await start_handler(message)
        return
    elif len(message.text) != 10:
        await message.answer(strings.INVALID_ID_TEXT)
        return
    async with state.proxy() as data:
        data['payment_id'] = message.text
        try:
            active = db.child("telebirr").child(message.text).get().val()
            if active['active']:
                if data['sub_type'] == 'premium' and active['pay_amount'] < config.PREMIUM_AMOUNT:
                    db.child("telebirr").child(message.text).update({'active': False})
                    await message.answer(strings.LESS_PAY_TEXT)
                    return
                if data['sub_type'] == 'platinum' and active['pay_amount'] < config.PLATINUM_AMOUNT:
                    db.child("telebirr").child(message.text).update({'active': False})
                    await message.answer(strings.LESS_PAY_TEXT)
                    return
                txt = "Your account have been confirmed please use the below " \
                      "link to activate your account." \
                      "\nhttps://ahdrwa-frontend.herokuapp.com/confirm"
                await message.answer(txt)
                db.child("telebirr").child(message.text).update({'active': False})
                request("PUT", config.API_URL_SUB, data={
                    "id": data['user_id'],
                    "subscription_lvl": data['sub_type']
                })
                await state.finish()
            else:
                await message.answer(strings.INVALID_ID_TEXT)
        except TypeError:
            await message.answer(strings.INVALID_ID_TEXT)
