from aiogram import types, Router from aiogram.filters import CommandStart

admin_router = Router()

@admin_router.message(CommandStart()) async def admin_start_handler(message: types.Message): await message.answer("پنل ادمین فعال شد. لطفاً یکی از گزینه‌ها را انتخاب کنید:") # اینجا می‌تونی دکمه‌های شیشه‌ای مربوط به ادمین رو اضافه کنی


