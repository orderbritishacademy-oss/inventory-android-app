from .files import load_json, save_json

def recompute_ledger():
    ledger = {}
    purchases = load_json("purchase.json", [])
    sales = load_json("sale.json", [])

    for p in purchases:
        ledger.setdefault(p["party"], 0)
        ledger[p["party"]] += p["total"]

    for s in sales:
        ledger.setdefault(s["party"], 0)
        ledger[s["party"]] -= s["total"]

    save_json("ledger.json", ledger)
    return ledger
