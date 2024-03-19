import json
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)



class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = []

        for product in products:
            product_obj = Product(product['name'], product['description'], product['price'], product['quantity'])
            self.products.append(product_obj)

        Category.total_categories += 1
        Category.total_unique_products += len(self.products)

    def product(self):
        for i in range(len(self.products)):
            return f"{self.products[i].name}, {self.products[i].price} руб. Остаток: {self.products[i].quantity} шт."


class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_products += 1

    @classmethod
    def get_prooduct(cls, name, description, price, quantity):
        product = cls(name, description, price, quantity)
        return product


    def set_price(self,price):
        if price < 0 or type(price) not in (int,float):
            print("Введена некорректная цена")
        else:
            self.price = price

    def get_price(self):
        return self.price



categories = []
for entry in data:
    category = Category(entry['name'], entry['description'], entry['products'])
    categories.append(category)




