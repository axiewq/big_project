class Category():
    title = str
    decription = str
    products = dict
    all_categories = int
    all_products = int

    def __init__(self, title, description, products):
        self.title = title
        self.decription = description
        self.products = products


class Product():
    title = str
    description = str
    price = float
    quantity = int

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
