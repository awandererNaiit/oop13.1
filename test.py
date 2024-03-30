import pytest

from main import Category, Product


def test_category():
    category = Category('овощи', 'огурчик рик')
    assert category.name == "овощи"
    assert category.description == "огурчик рик"
    assert category.products == []


def test_product():
    product = Product("овощи", "огурчик рик", 1000, 10)
    assert product.name == "овощи"
    assert product.description == "огурчик рик"
    assert product.price == 1000
    assert product.amount == 10


def test_product_count():
    category = Category("овощи", "огурчик рик")
    product1 = Product("фрукт", "морти", 1000, 10)
    product2 = Product("мультфильм", "развлечение на 5 минут", 1500, 5)
    category.products.append(product1)
    category.products.append(product2)
    assert len(category.products) == 2
