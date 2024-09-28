from aiogram import types
from aiogram.dispatcher import Dispatcher


async def cmd_info(message: types.Message):
    info_text = (
        "Это бот для управления продуктами и заказами.\n"
        "Команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/info - Получить информацию о боте\n"
        "/order - Сделать заказ\n"
        "/add_product - Добавить новый продукт (доступно только для сотрудников)\n"
        "/products - Просмотреть все товары"
    )
    await message.answer(info_text)


def register_info_handler(dp: Dispatcher):
    dp.register_message_handler(cmd_info, commands=['info'])
