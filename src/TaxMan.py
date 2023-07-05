class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = tax

    def calc_total(self):
        total = 0
        tax = float(self.tax.strip("%")) / 100
        for item in self.items:
            total += item['price'] + (tax * item['price'])
        return total
    def get_total(self):
        return self.calc_total()



