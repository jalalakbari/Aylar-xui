#!/bin/bash

set -e

echo "بروزرسانی لیست پکیج‌ها و نصب پیش‌نیازها..."
apt update && apt install -y python3 python3-pip git curl

echo "کلون کردن پروژه از گیت‌هاب..."
rm -rf /opt/aylar-xui
git clone https://github.com/jalalakbari/Aylar-xui.git /opt/aylar-xui

echo "نصب کتابخانه‌های پایتون..."
pip3 install --no-cache-dir -r /opt/aylar-xui/bot/requirements.txt

echo "لطفا اطلاعات زیر را وارد کنید:"
read -p "توکن ربات (BOT_TOKEN): " BOT_TOKEN
read -p "آی‌دی مالک/ادمین (ADMIN_ID): " ADMIN_ID
read -p "ساب‌دامین پنل (PANEL_SUBDOMAIN): " PANEL_SUBDOMAIN

echo "ساخت فایل کانفیگ config.json ..."
cat <<EOF > /opt/aylar-xui/bot/config.json
{
  "bot_token": "$BOT_TOKEN",
  "admin_id": $ADMIN_ID,
  "panel_domain": "$PANEL_SUBDOMAIN"
}
EOF

echo "ایجاد سرویس systemd برای ربات..."
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

echo "بارگذاری مجدد سرویس‌ها..."
systemctl daemon-reload

echo "فعال‌سازی سرویس aylar-xui..."
systemctl enable aylar-xui.service

echo "راه‌اندازی سرویس aylar-xui..."
systemctl start aylar-xui.service

echo "نصب با موفقیت انجام شد!"
echo "برای مشاهده وضعیت سرویس: sudo systemctl status aylar-xui"
