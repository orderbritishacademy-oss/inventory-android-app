from datetime import datetime
from .files import load_json, save_json
from .utils import invoice

def add_sale(party, products):
    db = load_json("sale.json", [])
    inv = invoice("S", len(db))
    total = sum(p["total"] for p in products)

    rec = {
        "id": len(db)+1,
        "invoice": inv,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "party": party,
        "products": products,
        "total": total
    }

    db.append(rec)
    save_json("sale.json", db)
    return rec

from .files import load_json, save_json

def get_purchases():
    return load_json("purchase.json", [])

def delete_purchase(pid):
    data = load_json("purchase.json", [])
    data = [p for p in data if p["id"] != pid]
    save_json("purchase.json", data)

def search_purchase(term):
    data = load_json("purchase.json", [])
    term = term.lower()
    return [p for p in data if term in p["party"].lower() or term in p["invoice"].lower()]

from logic.bills import create_bill

def generate_pdf(self):
    create_bill("INV001", self.ids.party.text, 1000)
