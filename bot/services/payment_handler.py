import json
from pathlib import Path

PAYMENT_FILE = Path("bot/data/payments.json")

def load_payments():
    if not PAYMENT_FILE.exists():
        return []
    with PAYMENT_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_payments(payments):
    with PAYMENT_FILE.open("w", encoding="utf-8") as f:
        json.dump(payments, f, indent=2, ensure_ascii=False)

def add_payment(payment_info: dict):
    payments = load_payments()
    payments.append(payment_info)
    save_payments(payments)

def get_pending_payments():
    payments = load_payments()
    return [p for p in payments if p.get("status") == "pending"]

def update_payment_status(payment_id, status):
    payments = load_payments()
    for p in payments:
        if p.get("id") == payment_id:
            p["status"] = status
    save_payments(payments)
