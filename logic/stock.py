from .files import load_json, save_json

def recompute_stock():
    purchases = load_json("purchase.json", [])
    sales = load_json("sale.json", [])

    stock = {}

    for p in purchases:
        for pr in p["products"]:
            stock.setdefault(pr["product"], 0)
            stock[pr["product"]] += pr["qty"]

    for s in sales:
        for pr in s["products"]:
            stock[pr["product"]] -= pr["qty"]

    save_json("stock.json", stock)
    return stock
