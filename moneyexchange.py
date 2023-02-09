class Price:
    def __init__(self, value: float or int):
        self.value = round(float(value), 2)

    @classmethod
    def from_usd(cls, value: float or int):
        pln = value*3.8
        return Price(pln)

    @classmethod
    def from_eur(cls, value: float or int):
        pln = value*4.5
        return Price(pln)

    def __str__(self):
        return f'{self.value} PLN'


some_price = Price.from_usd(25.50)
some_other_price = Price.from_eur(80)
print(some_price)
print(some_other_price)