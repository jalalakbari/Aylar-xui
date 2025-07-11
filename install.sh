#!/bin/bash

apt update && apt install -y python3 python3-pip git curl

git clone https://github.com/jalalakbari/Aylar-xui.git /opt/aylar-xui

cd /opt/aylar-xui/bot

pip3 install -r requirements.txt

read -p "token bot: " BOT_TOKEN
read -p "Id addadi: " ADMIN_ID
read -p "sabdomin: " PANEL_SUBDOMAIN

cat <<EOF > config.json
{
  "bot_token": "$BOT_TOKEN",
  "admin_id": $ADMIN_ID,
  "panel_domain": "$PANEL_SUBDOMAIN"
}
EOF

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

systemctl daemon-reload
systemctl enable aylar-xui.service
systemctl start aylar-xui.service
