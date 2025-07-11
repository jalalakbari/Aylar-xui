#!/bin/bash
set -e

apt update
apt install -y curl python3 python3-pip git

if [ -d "/opt/aylar-xui" ]; then
  rm -rf /opt/aylar-xui
fi

git clone https://github.com/jalalakbari/Aylar-xui.git /opt/aylar-xui

cd /opt/aylar-xui/bot

pip3 install -r requirements.txt

read -p "توکن ربات را وارد کنید: " BOT_TOKEN
read -p "ایدی عددی ادمین را وارد کنید: " ADMIN_ID
read -p "ساب‌دامین پنل را وارد کنید: " PANEL_SUBDOMAIN

cat > config.json <<EOF
{
  "bot_token": "$BOT_TOKEN",
  "admin_id": $ADMIN_ID,
  "panel_domain": "$PANEL_SUBDOMAIN"
}
EOF

cat > /etc/systemd/system/aylar-xui.service <<EOF
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

systemctl daemon-reload
systemctl enable aylar-xui.service
systemctl start aylar-xui.service

echo "نصب و راه‌اندازی ربات با موفقیت انجام شد."
