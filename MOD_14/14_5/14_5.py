from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from crud_functions_1 import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_ = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_line2 = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
button_reg = KeyboardButton(text='Регистрация')
kb_.add(button_1)
kb_.add(button_line2)
kb_.add(button_buy)
kb_.add(button_reg)

kb = InlineKeyboardMarkup()
button_line = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_line2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button_line)
kb.add(button_line2)

ilkb = InlineKeyboardMarkup()
but_1 = InlineKeyboardButton(text='Product_1', callback_data='product_buying')
but_2 = InlineKeyboardButton(text='Product_2', callback_data='product_buying')
but_3 = InlineKeyboardButton(text='Product_3', callback_data='product_buying')
but_4 = InlineKeyboardButton(text='Product_4', callback_data='product_buying')
ilkb.add(but_1)
ilkb.add(but_2)
ilkb.add(but_3)
ilkb.add(but_4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


prod = get_all_products()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('file_1.png', 'rb') as file:
        await message.answer(f'Название:{prod[0][0]} | Описание: {prod[0][1]} | Стоимость: {prod[0][2]} руб.',
                             reply_markup=kb_)
        await message.answer_photo(file, reply_markup=kb_)
    with open('file_2.png', 'rb') as file:
        await message.answer(f'Название:{prod[1][0]} | Описание: {prod[1][1]} | Стоимость: {prod[1][2]} руб.',
                             reply_markup=kb_)
        await message.answer_photo(file, reply_markup=kb_)
    with open('file_3.png', 'rb') as file:
        await message.answer(f'Название:{prod[2][0]} | Описание: {prod[2][1]} | Стоимость: {prod[2][2]} руб.',
                             reply_markup=kb_)
        await message.answer_photo(file, reply_markup=kb_)
    with open('file_4.png', 'rb') as file:
        await message.answer(f'Название:{prod[3][0]} | Описание: {prod[3][1]} | Стоимость: {prod[3][2]} руб.',
                             reply_markup=kb_)
        await message.answer_photo(file, reply_markup=kb_)
    await message.answer('Выберите продукт для покупки', reply_markup=ilkb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!!')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calorie_allowance = int(10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (5 * int(data['age'])) + 5
    await message.answer(f'Ваша норма калорий: {calorie_allowance}')
    await state.finish()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    data = await state.get_data()
    x = is_included(data['username'])
    if x is True:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await state.finish()


@dp.message_handler()
async def all_mes(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
