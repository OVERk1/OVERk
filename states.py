from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class User_States(StatesGroup):
    send_name = State()
    send_age = State()
    send_photo = State()
    send_description = State()