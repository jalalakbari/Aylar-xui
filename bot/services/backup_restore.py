import json
from pathlib import Path
import shutil
import datetime

DATA_DIR = Path("bot/data")
BACKUP_DIR = Path("bot/backups")

def create_backup():
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"backup_{timestamp}.zip"
    shutil.make_archive(str(backup_path).replace('.zip', ''), 'zip', DATA_DIR)
    return backup_path

def restore_backup(backup_file: Path):
    if not backup_file.exists():
        raise FileNotFoundError("Backup file not found")
    # Extract backup to data directory (overwrite existing)
    shutil.unpack_archive(str(backup_file), str(DATA_DIR))
