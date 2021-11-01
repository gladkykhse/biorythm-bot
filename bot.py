from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import API_TOKEN
from bio_image import createImage
import logging
import os

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    date = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Hello, I am Biorythm Cycle Bot.\nType /help to get the list of all commands')

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply('List of all commands:\n/bio - Get your current biorythm graph')

@dp.message_handler(commands='bio')
async def cmd_start(message: types.Message):
    await Form.date.set()
    await message.reply("Enter the date of birth in format YYYY.MM.DD")

@dp.message_handler(state=Form.date)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    createImage(data['date'],str(message.from_user.id))
    img = open(str(message.from_user.id)+".png","rb")
    await bot.send_photo(message.from_user.id, img, reply_to_message_id=message.message_id)
    os.remove(str(message.from_user.id)+".png")
    await state.finish()

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)