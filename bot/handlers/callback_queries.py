from aiogram import types, Router
from aiogram.filters import Text

callback_router = Router()

@callback_router.callback_query(Text(startswith="user_"))
async def user_callback_handler(callback: types.CallbackQuery):
    data = callback.data
    if data == "user_view_config":
        await callback.message.answer("نمایش کانفیگ شما ...")
        # TODO: بارگذاری کانفیگ کاربر
    elif data == "user_renew":
        await callback.message.answer("فرآیند تمدید آغاز شد ...")
        # TODO: شروع فرآیند تمدید
    # می‌توانید دستورات بیشتری اضافه کنید

@callback_router.callback_query(Text(startswith="admin_"))
async def admin_callback_handler(callback: types.CallbackQuery):
    data = callback.data
    if data == "admin_manage_users":
        await callback.message.answer("بارگذاری کاربران برای مدیریت ...")
        # TODO: بارگذاری کاربران
    elif data == "admin_manage_payments":
        await callback.message.answer("بررسی فیش‌های پرداختی ...")
        # TODO: مدیریت فیش‌ها
    # سایر عملیات مدیریت

@callback_router.callback_query(Text(startswith="owner_"))
async def owner_callback_handler(callback: types.CallbackQuery):
    data = callback.data
    if data == "owner_add_server":
        await callback.message.answer("فرآیند افزودن سرور جدید آغاز شد ...")
        # TODO: افزودن سرور توسط مالک
    # عملیات دیگر مالک
