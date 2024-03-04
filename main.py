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


class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_products += 1

