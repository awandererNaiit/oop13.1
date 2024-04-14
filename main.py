class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.total_unique_products += 1

    def remove_product(self, product):
        self.__products.remove(product)
        Category.total_unique_products -= 1

    def get_products(self):
        return self.__products

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            product_info = f"{product.name}, {product.price} руб. Остаток: {product.amount} шт."
            products_info.append(product_info)
        return products_info


class Product:
    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.__price = price
        self.amount = amount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Ошибка: Цена должна быть больше нуля.")
        else:
            self.__price = new_price



