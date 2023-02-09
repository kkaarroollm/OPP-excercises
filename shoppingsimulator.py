class Product:
    unique_id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.unique_id
        Product.unique_id += 1


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        if product.id in self.products:
            self.quantities[product.id] += 1
        else:
            self.products[product.id] = product
            self.quantities[product.id] = 1

    def remove_product(self, product):
        if product.id in self.products:
            if self.quantities[product.id] > 1:
                self.quantities[product.id] -= 1
            else:
                del self.products[product.id]
        else:
            pass

    def change_product_quantity(self, product, new_quantity):
        if product.id in self.products:
            if new_quantity == 0:
                del self.products[product.id]
                del self.quantities[product.id]
            if new_quantity < 0:
                raise ValueError("u cant remove less than 0 items lol")
            else:
                self.quantities[product.id] = new_quantity
        else:
            pass

    def get_receipt(self):
        receipt = ''
        total = 0
        for product in self.products:
            product = self.products.get(product)
            name = product.name
            price = product.price
            quantity = self.quantities.get(product.id)
            total += price * quantity
            if quantity >= 3:
                receipt += f'{name} - amount: {quantity}, ' \
                       f'price: {price}, total: {round(quantity * price*0.7, 1)}, SALE!\n'
            else:
                receipt += f'{name} - amount: {quantity}, ' \
                            f'price: {price}, total: {round(quantity * price, 1)}\n'
        receipt += f'Total: {round(total, 2)}'
        return receipt


apple = Product('Apple', 3.99)
bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)
cart = ShoppingCart()
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chive)
cart.add_product(apple)
print(cart.get_receipt())
