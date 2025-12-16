from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

from logic.purchase import add_purchase, get_purchases, delete_purchase, search_purchase
from logic.sale import add_sale
from logic.stock import recompute_stock
from logic.ledger import recompute_ledger
from logic.files import load_json


# ✅ DEFINE SCREENS FIRST (VERY IMPORTANT)

class BgScreen(Screen):
    pass


class Dashboard(BgScreen):
    pass


class Purchase(BgScreen):
    selected_id = None

    def on_pre_enter(self):
        self.load_list()

    def save_purchase(self):
        party = self.ids.party.text
        product = self.ids.product.text
        qty = float(self.ids.qty.text)
        rate = float(self.ids.rate.text)

        products = [{
            "product": product,
            "qty": qty,
            "rate": rate,
            "total": qty * rate
        }]

        add_purchase(party, products)
        recompute_stock()
        recompute_ledger()
        self.load_list()

    def load_list(self, items=None):
        self.ids.list.clear_widgets()
        data = items if items else get_purchases()

        for p in data:
            btn = Button(
                text=f"{p['invoice']} | {p['party']} | ₹{p['total']}",
                size_hint_y=None,
                height="40dp"
            )
            btn.bind(on_release=lambda x, pid=p["id"]: self.select(pid))
            self.ids.list.add_widget(btn)

    def select(self, pid):
        self.selected_id = pid

    def delete_selected(self):
        if self.selected_id:
            delete_purchase(self.selected_id)
            self.selected_id = None
            self.load_list()

    def search(self, txt):
        self.load_list(search_purchase(txt))


class Sale(BgScreen):
    def save_sale(self):
        party = self.ids.party.text
        product = self.ids.product.text
        qty = float(self.ids.qty.text)
        rate = float(self.ids.rate.text)

        products = [{
            "product": product,
            "qty": qty,
            "rate": rate,
            "total": qty * rate
        }]

        add_sale(party, products)
        recompute_stock()
        recompute_ledger()


class Stock(BgScreen):
    def on_pre_enter(self):
        self.ids.stock_list.clear_widgets()
        stock = load_json("stock.json", {})
        for name, qty in stock.items():
            self.ids.stock_list.add_widget(
                Label(text=f"{name} : {qty}", size_hint_y=None, height="30dp")
            )


class Ledger(BgScreen):
    def on_pre_enter(self):
        self.ids.ledger_list.clear_widgets()
        ledger = load_json("ledger.json", {})
        for party, bal in ledger.items():
            self.ids.ledger_list.add_widget(
                Label(text=f"{party} : ₹ {bal}", size_hint_y=None, height="30dp")
            )


# ✅ LOAD KV FILE AFTER CLASSES EXIST
Builder.load_file("inventory.kv")


class InventoryApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Dashboard(name="dashboard"))
        sm.add_widget(Purchase(name="purchase"))
        sm.add_widget(Sale(name="sale"))
        sm.add_widget(Stock(name="stock"))
        sm.add_widget(Ledger(name="ledger"))
        return sm


InventoryApp().run()
