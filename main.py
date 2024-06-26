import json
from abc import ABC, abstractmethod

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class AllProducts(ABC):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def get_product(cls, name, description, price, quantity):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinLog:
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        print(f'Был создан такой продукт:\n{self.name}, {self.description}, {self.price}, {self.quantity}')


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.products = products
        self.name = name
        self.description = description
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def calculate_average_price(self):
        try:
            if len(self.products) == 0:
                raise ZeroDivisionError
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.products)}'

    def __len__(self):
        counter = 0
        for product in self.products:
            counter += product.quantity
        return counter

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            Category.total_unique_products += 1
        else:
            raise TypeError

    @property
    def product(self):
        return '\n'.join(map(str, self.products))


class Product(MixinLog, AllProducts):
    total_products = 0

    def __init__(self, name, description, price, quantity):
        try:
            if not quantity or quantity <= 0:
                raise ValueError
        except ValueError:
            print(f'в {name} количество должно быть положительным, продукт не создан')
        else:
            super().__init__(name, description, price, quantity)
            Product.total_products += 1

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError

    @classmethod
    def get_product(cls, name, description, price, quantity):
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


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, internal_memory, colour):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory
        self.colour = colour


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, growth_time, colour):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.growth_time = growth_time
        self.colour = colour


# categories = []
# for entry in data:
#     products = []
#     for prod in entry['products']:
#         product = Product(prod['name'], prod['description'], prod['price'], prod['quantity'])
#         products.append(product)
#     category = Category(entry['name'], entry['description'], products)
#     categories.append(category)
#
# for category in categories:
#     print(category)
#     print(len(category))
c = LawnGrass('trava', 'default', 300, 87213, 'USA', 2, 'zelen')
z = Smartphone('salad', 'food', 5000, 2, '10000', 'Samsung', 300, 'black')
m = LawnGrass('marihuana', 'drug', 2500, 123, 'Afganistan', 10, 'beautiful')

