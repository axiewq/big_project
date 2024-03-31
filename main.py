import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.products = products
        self.name = name
        self.description = description
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self.products)}'

    def __len__(self):
        counter = 0
        for product in self.products:
            counter += product.quantity
        return counter

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products += 1

    @property
    def product(self):
        return '\n'.join(map(str, self.products))


class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_products += 1

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


categories = []
for entry in data:
    products = []
    for prod in entry['products']:
        product = Product(prod['name'], prod['description'], prod['price'], prod['quantity'])
        products.append(product)
    category = Category(entry['name'], entry['description'], products)
    categories.append(category)

for category in categories:
    print(category)
    print(len(category))
