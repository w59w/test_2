from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher
from config import STAFF_IDS  


class OrderFSM(StatesGroup):
    article = State()  
    size = State()     
    quantity = State() 
    contact = State()  


async def start_order(message: types.Message):
    await OrderFSM.article.set() 
    await message.answer("Введите артикул товара, который хотите заказать:", reply_markup=types.ReplyKeyboardRemove())


async def process_article(message: types.Message, state: FSMContext):
    await state.update_data(article=message.text)  
    await OrderFSM.next()  
    await message.answer("Введите размер товара:")


async def process_size(message: types.Message, state: FSMContext):
    await state.update_data(size=message.text)  
    await OrderFSM.next()  
    await message.answer("Введите количество товара:")


async def process_quantity(message: types.Message, state: FSMContext):
    await state.update_data(quantity=message.text) 
    await OrderFSM.next() 
    await message.answer("Введите ваш контактный номер телефона:")


async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)  

 
    data = await state.get_data()

  
    order_info = (
        f"Новый заказ:\n\n"
        f"Артикул: {data['article']}\n"
        f"Размер: {data['size']}\n"
        f"Количество: {data['quantity']}\n"
        f"Контактные данные: {data['contact']}"
    )


    for staff_id in STAFF_IDS:
        try:
            await message.bot.send_message(staff_id, order_info)
        except Exception as e:
            await message.answer(f"Ошибка при отправке данных сотруднику с ID {staff_id}: {e}")


    await message.answer("Ваш заказ принят! Ожидайте подтверждения.", reply_markup=types.ReplyKeyboardRemove())

    await state.finish()


def register_order_handlers(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'], state=None)  
    dp.register_message_handler(process_article, state=OrderFSM.article) 
    dp.register_message_handler(process_size, state=OrderFSM.size)  
    dp.register_message_handler(process_quantity, state=OrderFSM.quantity)  
    dp.register_message_handler(process_contact, state=OrderFSM.contact)  

