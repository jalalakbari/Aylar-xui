import json
from pathlib import Path

SERVERS_FILE = Path("bot/data/servers.json")

def load_servers():
    if not SERVERS_FILE.exists():
        return []
    with SERVERS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_servers(servers):
    with SERVERS_FILE.open("w", encoding="utf-8") as f:
        json.dump(servers, f, indent=2, ensure_ascii=False)

def add_server(server_info: dict):
    servers = load_servers()
    if any(s["id"] == server_info["id"] for s in servers):
        return False
    servers.append(server_info)
    save_servers(servers)
    return True

def remove_server(server_id):
    servers = load_servers()
    servers = [s for s in servers if s["id"] != server_id]
    save_servers(servers)

def get_server_by_id(server_id):
    servers = load_servers()
    for s in servers:
        if s["id"] == server_id:
            return s
    return None
