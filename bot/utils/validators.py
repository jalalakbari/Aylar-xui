import re

def validate_username(username: str):
    # فقط حروف، اعداد و _ قبول است
    return re.match(r'^\w+$', username) is not None

def validate_phone(phone: str):
    # الگوی ساده شماره تلفن (مثلا 10 تا 15 رقم)
    return re.match(r'^\d{10,15}$', phone) is not None
