from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher
from config import STAFF_IDS  


class ProductFSM(StatesGroup):
    name = State()      
    category = State()  
    size = State()      
    price = State()   
    article = State()   
    photo = State()    


def register_product_handlers(dp: Dispatcher):
    dp.register_message_handler(add_product, commands=['add_product'], state=None)  
    dp.register_message_handler(process_product_name, state=ProductFSM.name)


async def add_product(message: types.Message):
    if message.from_user.id in STAFF_IDS:
        await ProductFSM.name.set()
        await message.answer("Введите название продукта:")
    else:
        await message.answer("У вас нет доступа для добавления продуктов.")
