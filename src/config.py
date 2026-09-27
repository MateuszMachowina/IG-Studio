import json
from pathlib import Path

CONFIG_FILE = Path("app_config.json")

def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except:
            pass
    return {"target_username": "", "session_id": ""}

def save_config(target_username, session_id, user_id=""):
    cfg = {"target_username": target_username, "session_id": session_id, "user_id": user_id}
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
