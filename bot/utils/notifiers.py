from telegram import Bot

def notify_owner(bot: Bot, owner_id: int, message: str):
    bot.send_message(chat_id=owner_id, text=message)

def notify_admins(bot: Bot, admin_ids: list, message: str):
    for admin_id in admin_ids:
        bot.send_message(chat_id=admin_id, text=message)
