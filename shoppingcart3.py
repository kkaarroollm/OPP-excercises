class Cart:
    def __init__(self):
        self.products = []

    def add(self, price: [int, float], product: str):
        return self.products.append((price, product))

    def summary(self):
        return self.products


class Discount20percent(Cart):
    def summary(self):
        products = [(price * 0.8, name) for price, name in self.products]
        return products


class Above3ProductsCheapestFreeCart(Cart):

    def summary(self):
        products = []
        if len(self.products) > 3:
            for x in self.products:
                if x == self.products[0]:
                    lst = list(x)
                    lst[0] = 0
                    products.append(tuple(lst))
                else:
                    products.append(x)

        return products

# a = Cart()
# a.add(3.99, 'ananas')
# a.add(182.43, 'myszka')
# a.add(34, 'kabel')
# print(a.summary())
#
# a = Discount20percent()
# a.add(3.99, 'ananas')
# a.add(182.43, 'myszka')
# a.add(34, 'kabel')
# print(a.summary())
#
# a = Above3ProductsCheapestFreeCart()
# a.add(3.99, 'ananas')
# a.add(182.43, 'myszka')
# a.add(34, 'kabel')
# a.add(35, 'ala')
# print(a.summary())