import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.__products = products.copy()  # Создаем копию списка продуктов
        self.name = name
        self.description = description

        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

    def get_product_info(self):
        for product in self.__products:
            info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            print(info)


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

    @property
    def price(self):
        return self.price

    price.setter
    def price(self, price):
        if price < 0 or type(price) not in (int, float):
            print("Введена некорректная цена")
        else:
            self.price = price


categories = []
for entry in data:
    category = Category(entry['name'], entry['description'], entry['products'])
    categories.append(category)
