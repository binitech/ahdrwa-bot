from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStatus(StatesGroup):
    user_id = State()
    sub_type = State()
    payment_method = State()
    payment_id = State()
