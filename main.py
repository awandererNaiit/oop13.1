class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

        Category.total_categories += 1


class Product:
    name: str
    description: str
    products: list
    price: int
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount




