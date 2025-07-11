#!/bin/bash

set -e

# به‌روزرسانی و نصب پیش‌نیازها
apt update
apt install -y python3 python3-pip git curl

# حذف پوشه قبلی در صورت وجود
if [ -d "/opt/aylar-xui" ]; then
  rm -rf /opt/aylar-xui
fi

# کلون کردن ریپازیتوری
git clone https://github.com/jalalakbari/Aylar-xui.git /opt/aylar-xui

# ورود به پوشه بات
cd /opt/aylar-xui/bot

# نصب وابستگی‌ها
pip3 install -r requirements.txt

# گرفتن ورودی کاربر
read -p "توکن ربات را وارد کنید: " BOT_TOKEN
read -p "ایدی عددی ادمین را وارد کنید: " ADMIN_ID
read -p "ساب‌دامین پنل را وارد کنید: " PANEL_SUBDOMAIN

# ایجاد فایل کانفیگ
cat <<EOF > config.json
{
  "bot_token": "$BOT_TOKEN",
  "admin_id": $ADMIN_ID,
  "panel_domain": "$PANEL_SUBDOMAIN"
}
EOF

# ایجاد سرویس systemd برای اجرای ربات
cat <<EOF > /etc/systemd/system/aylar-xui.service
[Unit]
Description=Aylar-xui Telegram Bot
After=network.target

[Service]
User=root
WorkingDirectory=/opt/aylar-xui/bot
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# بارگذاری مجدد systemd، فعال و استارت سرویس
systemctl daemon-reload
systemctl enable aylar-xui.service
systemctl start aylar-xui.service

echo "نصب و راه‌اندازی ربات با موفقیت انجام شد."
