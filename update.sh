#!/bin/bash

set -e

SERVICE_NAME="aylar-xui.service"
APP_DIR="/opt/aylar-xui"

echo "Stopping service..."
sudo systemctl stop $SERVICE_NAME

echo "Updating source code from GitHub..."
cd $APP_DIR

git pull https://github.com/jalalakbari/Aylar-xui.git main

echo "Installing dependencies if needed..."
# نمونه برای پایتون یا نود؛ این خط رو به پروژه خودت تنظیم کن
# pip install -r requirements.txt

echo "Starting service..."
sudo systemctl start $SERVICE_NAME

echo "Update completed successfully."
