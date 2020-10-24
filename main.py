import logging, random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram.utils.helper import Helper, HelperMode, ListItem
import amat

logging.basicConfig(level=logging.INFO)

bot = Bot(token='1337088673:AAFVcbSKpYLsvVqPy1eAjeBml0Ho5_jrlHA')
dp = Dispatcher(bot, storage=MemoryStorage())


##dp.middleware.setup(LoggingMiddleware())


class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()
    TEST_STATE_6 = ListItem()


@dp.message_handler(commands=['start'])
async def fg(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    await message.reply('введите имя')
    await state.set_state(TestStates.all()[0])


@dp.message_handler(state=TestStates.TEST_STATE_0)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        print(1)
        await message.answer('я всё твоей маме расскажу')
        await state.set_state(TestStates.all()[1])
    else:
        await state.set_state(TestStates.all()[6])
        print(2)


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        await message.answer('сделал скриншот')
        await state.set_state(TestStates.all()[2])


@dp.message_handler(state=TestStates.TEST_STATE_2)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        await message.answer('Отправил')
        await state.set_state(TestStates.all()[3])


@dp.message_handler(state=TestStates.TEST_STATE_3)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        await message.answer('Очередное неотесоное быдло')
        await state.set_state(TestStates.all()[4])


@dp.message_handler(state=TestStates.TEST_STATE_4)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        await  message.answer_sticker('CAACAgIAAxkBAAI5pl-UB2XnSUmiOzLWIx0vlSg2_YaOAAKRAAPkoM4H4iu9K4yuq9YbBA')
        await state.set_state(TestStates.all()[5])


@dp.message_handler(state=TestStates.TEST_STATE_5)
async def ma(message: types.message):
    state = dp.current_state(user=message.from_user.id)
    m = message.text
    if not amat.cyctem(m):
        print(1)
        await message.answer_sticker('CAACAgIAAxkBAAI5ml-T9poSqyFXdtycOalUBjny4E3jAAIOAAPANk8TI1cURIdu1mUbBA')


@dp.message_handler(state=TestStates.TEST_STATE_6)
async def ma(message: types.message):
    await message.answer('Извини у меня не бесконечные возможность')
    await message.answer('програмистам было лень создать мне искуственый интелект')
    await message.answer_sticker('CAACAgIAAxkBAAI6CF-UgiXyyPkJ0djfigjKq_H8svV0AAIKBwACRvusBFNTipZg0G-tGwQ')


@dp.message_handler(commands=['билеты'])
async def ma(message: types.message):
    while message.text != 'стоп':
        md = ['сложно']
        md.append(message.text)
        print(md)
    secure_random = random.SystemRandom()
    await message.answer(secure_random)


if __name__ == '__main__':
    executor.start_polling(dp)
