import pytest
from main import Category, Product


# Тесты для класса Category
def test_category_init():
    category = Category('Смартфоны', 'Описание', [
        {'name': 'Product 1', 'description': 'Description 1', 'price': 100.0, 'quantity': 5},
        {'name': 'Product 2', 'description': 'Description 2', 'price': 200.0, 'quantity': 10}
    ])

    assert category.name == 'Смартфоны'
    assert category.description == 'Описание'
    assert len(category.products) == 2


def test_category_total_categories():
    initial_total = Category.total_categories

    category1 = Category('Category 1', 'Description 1', [])
    assert Category.total_categories == initial_total + 1

    category2 = Category('Category 2', 'Description 2', [])
    assert Category.total_categories == initial_total + 2


def test_category_total_unique_products():
    initial_total = Category.total_unique_products

    category = Category('Смартфоны', 'Описание', [
        {'name': 'Product 1', 'description': 'Description 1', 'price': 100.0, 'quantity': 5},
        {'name': 'Product 2', 'description': 'Description 2', 'price': 200.0, 'quantity': 10}
    ])
    assert Category.total_unique_products == initial_total + 2


# Тесты для класса Product
def test_product_init():
    product = Product('Product 1', 'Description', 100.0, 5)

    assert product.name == 'Product 1'
    assert product.description == 'Description'
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_total_products():
    initial_total = Product.total_products

    product1 = Product('Product 1', 'Description 1', 100.0, 5)
    assert Product.total_products == initial_total + 1

    product2 = Product('Product 2', 'Description 2', 200.0, 10)
    assert Product.total_products == initial_total + 2


# Запуск всех тестов
if __name__ == '__main__':
    pytest.main()
