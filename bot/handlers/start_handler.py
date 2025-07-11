from aiogram import types from aiogram.dispatcher import Dispatcher from utils.validators import is_owner, is_admin from handlers.owner_handler import owner_panel from handlers.admin_handler import admin_panel from handlers.user_handler import user_panel

def register_start_handler(dp: Dispatcher): @dp.message_handler(commands=['start']) async def handle_start(message: types.Message): user_id = message.from_user.id

if is_owner(user_id):
        await message.answer("\u2705 خوش آمدید به پنل مدیریت اصلی.")
        await owner_panel(message)

    elif is_admin(user_id):
        await message.answer("\ud83d\udc68\u200d\ud83d\udcbc خوش آمدید به پنل ادمین.")
        await admin_panel(message)

    else:
        await message.answer("\ud83d\udcc5 خوش آمدید! لطفا از دکمه‌های زیر استفاده کنید.")
        await user_panel(message)

