from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_ = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_line2 = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
kb_.add(button_1)
kb_.add(button_line2)
kb_.add(button_buy)

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


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb_)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(4):
        with open(f'file_{i + 1}.png', 'rb') as photo:
            await message.answer(f'Название: Product_{i + 1} | Описание: описание {i + 1} | Стоимость: {(i + 1) * 100}',
                                 reply_markup=kb_)
            await message.answer_photo(photo, reply_markup=kb_)
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


@dp.message_handler()
async def all_mes(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
