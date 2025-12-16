from datetime import datetime

def calc_totals(qty, rate, disc=0, tax=0):
    subtotal = qty * rate
    discount = subtotal * (disc / 100)
    taxable = subtotal - discount
    tax_amt = taxable * (tax / 100)
    total = taxable + tax_amt
    return round(subtotal,2), round(discount,2), round(tax_amt,2), round(total,2)

def invoice(prefix, count):
    return f"{prefix}{datetime.now().strftime('%y%m%d')}{count+1}"
