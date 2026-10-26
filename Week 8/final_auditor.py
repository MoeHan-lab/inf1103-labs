import json

INVENTORY_FILE = "inventory.json"

class Product:
    def __init__(self, product_id, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = 0
        self.update_stock(stock)  
 
    def get_product_id(self):
        return self.__product_id
 
    def get_name(self):
        return self.__name
 
    def get_price(self):
        return self.__price
 
    def get_stock(self):
        return self.__stock
 
    def update_stock(self, quantity):
        """Set the stock level. Stock must be a non-negative whole number."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity
 
    def display_information(self):
        """Print this product's details on one line."""
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
