import json
from pathlib import Path

ADMIN_FILE = Path("bot/data/admins.json")

def load_admins():
    if not ADMIN_FILE.exists():
        return []
    with ADMIN_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_admins(admins):
    with ADMIN_FILE.open("w", encoding="utf-8") as f:
        json.dump(admins, f, indent=2, ensure_ascii=False)

def is_admin(user_id: int):
    admins = load_admins()
    return any(admin["id"] == user_id for admin in admins)

def add_admin(admin_info: dict):
    admins = load_admins()
    if any(admin["id"] == admin_info["id"] for admin in admins):
        return False
    admins.append(admin_info)
    save_admins(admins)
    return True

def remove_admin(user_id: int):
    admins = load_admins()
    admins = [a for a in admins if a["id"] != user_id]
    save_admins(admins)
