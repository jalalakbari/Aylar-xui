from aiogram import types, Router from aiogram.filters import Command

owner_router = Router()

@owner_router.message(Command("owner")) async def owner_panel(message: types.Message): keyboard = types.InlineKeyboardMarkup(inline_keyboard=[ [types.InlineKeyboardButton(text="➕ افزودن سرور", callback_data="add_server")], [types.InlineKeyboardButton(text="👥 مدیریت ادمین‌ها", callback_data="manage_admins")], [types.InlineKeyboardButton(text="📊 گزارش فروش", callback_data="view_sales")], [types.InlineKeyboardButton(text="💰 مدیریت پرداختی‌ها", callback_data="manage_payments")], [types.InlineKeyboardButton(text="🔧 تنظیمات قیمت‌ها", callback_data="edit_prices")], [types.InlineKeyboardButton(text="📦 بکاپ / ریستور", callback_data="backup_restore")], [types.InlineKeyboardButton(text="🔄 بروزرسانی ربات", callback_data="update_bot")] ]) await message.answer("پنل مدیریت مالک:", reply_markup=keyboard)

