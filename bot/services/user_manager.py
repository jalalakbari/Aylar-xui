import json
from pathlib import Path

USERS_FILE = Path("bot/data/users.json")

def load_users():
    if not USERS_FILE.exists():
        return []
    with USERS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def add_user(user_info: dict):
    users = load_users()
    if any(u["id"] == user_info["id"] for u in users):
        return False
    users.append(user_info)
    save_users(users)
    return True

def update_user(user_id, updated_info):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            user.update(updated_info)
            save_users(users)
            return True
    return False

def get_user_by_id(user_id):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def delete_user(user_id):
    users = load_users()
    users = [u for u in users if u["id"] != user_id]
    save_users(users)
