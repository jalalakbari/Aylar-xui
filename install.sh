#!/bin/bash
set -euo pipefail

# لاگ فایل
LOG_FILE="/var/log/aylar-xui-install.log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "شروع نصب Aylar-xui..."

# به‌روزرسانی و نصب پیش‌نیازها
echo "آپدیت بسته‌ها و نصب پیش‌نیازها..."
apt-get update -y
apt-get install -y python3 python3-pip git curl

# حذف نسخه قبلی در صورت وجود
if [ -d "/opt/aylar-xui" ]; then
  echo "پاکسازی نسخه قبلی..."
  rm -rf /opt/aylar-xui
fi

# کلون ریپازیتوری
echo "کلون کردن پروژه از گیت‌هاب..."
git clone https://github.com/jalalakbari/Aylar-xui.git /opt/aylar-xui

# نصب وابستگی‌های پایتون
echo "نصب وابستگی‌ها..."
pip3 install --no-cache-dir -r /opt/aylar-xui/bot/requirements.txt

# دریافت اطلاعات کاربر
read -rp "توکن ربات را وارد کنید: " BOT_TOKEN
read -rp "ایدی عددی ادمین را وارد کنید: " ADMIN_ID
read -rp "ساب‌دامین پنل را وارد کنید: " PANEL_SUBDOMAIN

# ایجاد فایل تنظیمات
cat > /opt/aylar-xui/bot/config.json <<EOF
{
  "bot_token": "$BOT_TOKEN",
  "admin_id": $ADMIN_ID,
  "panel_domain": "$PANEL_SUBDOMAIN"
}
EOF

# ایجاد سرویس systemd
echo "ایجاد سرویس systemd برای ربات..."
cat > /etc/systemd/system/aylar-xui.service <<EOF
[Unit]
Description=Aylar-xui Telegram Bot
After=network.target

[Service]
User=root
WorkingDirectory=/opt/aylar-xui/bot
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# بارگذاری مجدد systemd و فعال‌سازی سرویس
echo "بارگذاری مجدد systemd و شروع سرویس..."
systemctl daemon-reload
systemctl enable aylar-xui.service
systemctl start aylar-xui.service

echo "نصب با موفقیت انجام شد! برای مشاهده لاگ‌ها: sudo tail -f $LOG_FILE"
