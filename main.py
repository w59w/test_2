from aiogram import executor
from config import dp 
from handlers.fsm_order import register_order_handlers  
from handlers.fsm_product import register_product_handlers 
from handlers.start_handler import register_start_handler  
from handlers.info_handler import register_info_handler  


register_order_handlers(dp)
register_product_handlers(dp)  
register_start_handler(dp)  
register_info_handler(dp)  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
