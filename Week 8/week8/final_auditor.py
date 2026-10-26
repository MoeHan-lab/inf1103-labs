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
        
class Inventory:
    """Manages a collection of Product objects."""
 
    LINE_WIDTH = 47
 
    def __init__(self):
        self.__products = []
 
    def add_product(self, product):
        """Add a Product. Returns False if the ID already exists, else True."""
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the inventory.")
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True
 
    def find_product(self, product_id):
        """Return the Product with this ID (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None
 
    def search_product(self, keyword):
        """Return a list of Products whose ID matches or whose name contains keyword."""
        keyword = keyword.strip().lower()
        return [p for p in self.__products
                if keyword == p.get_product_id().lower() or keyword in p.get_name().lower()]
 
    def get_products(self):
        """Return a copy of the product list (so callers can't alter the original)."""
        return list(self.__products)
 
    def display_products(self, products, title):
        """Print a titled list of the given products."""
        print(f"\n{title}")
        print("-" * self.LINE_WIDTH)
        if not products:
            print("Inventory is empty.")
        else:
            for product in products:
                product.display_information()
        print("-" * self.LINE_WIDTH)
 
    def display_all(self):
        """Print every product in the inventory."""
        self.display_products(self.__products, "Current Inventory")