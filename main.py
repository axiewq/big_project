import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.__products = products
        self.name = name
        self.description = description
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.__products)}'

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def product(self):
        return '\n'.join(map(str,self.__products))


class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.total_products += 1

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity
    @classmethod
    def get_prooduct(cls, name, description, price, quantity):
        product = cls(name, description, price, quantity)
        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if int(price) < 0 or type(price) not in (int, float):
            print("Введена некорректная цена")
        else:
            self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


categories = []
for entry in data:
    category = Product(entry['name'], entry['description'],entry['price'], entry['products'],)
    categories.append(category)




