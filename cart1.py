class Cart:
    def __init__(self):
        self.products = []

    def add(self, price: float, price_tag: str):
        self.products.append((price, price_tag))

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        product20 = []
        for product in self.products:
            price = 0.8 * product[0]
            product20.append((price, product[1]))
        return product20


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) > 3:
            price, price_tag = min(self.products)
            cheapest = (0, price_tag)
            index = self.products.index(min(self.products))
            self.products[index] = cheapest
        return self.products

a = Cart()
a.add(14.23, 'jajo')
a.add(32.24, 'sol')
a.add(27.23, 'mleko')
a.add(4.23, 'kinder')

b = Discount20PercentCart()
b.add(14.23, 'jajo')
b.add(32.24, 'sol')
b.add(27.23, 'mleko')
b.add(4.23, 'kinder')
print(b.summary())

c = Above3ProductsCheapestFreeCart()
c.add(14.23, 'jajo')
c.add(32.24, 'sol')
c.add(27.23, 'mleko')
c.add(4.23, 'kinder')
print(c.summary())