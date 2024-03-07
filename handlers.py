

from keyboards import get_kb
from states import User_States

from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext



router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    await message.answer(text='Привет! Нажми на кнопку ниже, чтобы создать анкету',
                     reply_markup=get_kb())


#Создаем анкету
@router.message(StateFilter(None), F.text.lower()=='создать анкету')
async def create_profile(message:types.Message, state:FSMContext) -> None:
    await message.reply(text='Отлично! Сначала придумай себе имя')

    await state.set_state(User_States.send_name)

#Приимаем имя пользователя(send_name) и просим возраст
@router.message(StateFilter(User_States.send_name))
async def load_name(message:types.Message, state:FSMContext) -> None:
    if len(message.text)<20:
        await state.update_data(user_name=message.text.title())

        await message.reply(text='Теперь скажи свой возраст')

        await state.set_state(User_States.send_age)

    else:
        await message.reply(text='Введи реальное имя!')


#Принамаем возраст пользователя(send_age) и просим фото
@router.message(StateFilter(User_States.send_age))
async def load_age(message: types.Message, state: FSMContext) -> None:
    try:
        number = int(message.text)

        if number<100:
            await state.update_data(user_age=message.text.lower())
            await message.reply(text='А сейчас пришли своё фото')
            await state.set_state(User_States.send_photo)

        else:
            await message.reply(text='Введи реальный возраст!')

    except ValueError:
        await message.reply(text='Введи реальный возраст!')

#Принмаем фото пользователя(send_photo) и просим описание профиля

@router.message(StateFilter(User_States.send_photo))
async def load_photo(message:types.Message, state:FSMContext) -> None:
    if message.photo:
        await state.update_data(user_photo=message.photo[-1].file_id)
        await message.reply(text='Тебе также нужно добавить описание профиля(не более 60 слов)')

        await state.set_state(User_States.send_description)

    else:
        await message.reply(text='Это не фотография!')



#Принмаем описание профиля пользователя(send_description)
@router.message(StateFilter(User_States.send_description))
async def load_desc(message:types.Message, state:FSMContext) -> None:
    if len(message.text)<61:
        await state.update_data(user_desc=message.text)
        await message.reply(text='Супер! Ты создал свою анкету! Вот она')
        user_data = await state.get_data()
        print(user_data)
        await message.answer_photo(photo=f"{user_data['user_photo']}",
                                   caption=f"{user_data['user_name']},"
                                           f" {user_data['user_age']},\n"
                                           f" {user_data['user_desc']}")
        await state.clear()

    else:
        await message.reply(text='Ты превысил количество допустимых символов!')

















