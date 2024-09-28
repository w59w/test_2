from aiogram import types
from aiogram.dispatcher import Dispatcher


async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Используйте команды для взаимодействия с ботом.")


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
