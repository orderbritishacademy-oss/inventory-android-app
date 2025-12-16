import json, os

DATA = "data"
os.makedirs(DATA, exist_ok=True)

def load_json(name, default):
    path = os.path.join(DATA, name)

    if not os.path.exists(path):
        save_json(name, default)
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                save_json(name, default)
                return default
            return json.loads(content)
    except:
        save_json(name, default)
        return default


def save_json(name, data):
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
