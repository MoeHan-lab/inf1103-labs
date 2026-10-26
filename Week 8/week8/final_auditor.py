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

def load_inventory(filename):
    """Load an Inventory from a JSON file. Returns an empty Inventory on failure."""
    inventory = Inventory()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"{filename} found.")
        for item in data:
            try:
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"])
                )
            except (KeyError, TypeError, ValueError):
                print(f"WARNING: Skipped an invalid product entry: {item}")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty inventory.")
    except json.JSONDecodeError:
        print("ERROR: Could not read inventory file. Starting with an empty inventory.")
    return inventory
def save_inventory(inventory, filename):
    """Save an Inventory to a JSON file."""
    data = [
        {"id": p.get_product_id(), "name": p.get_name(), "price": p.get_price(), "stock": p.get_stock()}
        for p in inventory.get_products()
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved to {filename}.")

def save_inventory(inventory, filename):
    """Save an Inventory to a JSON file."""
    data = [
        {"id": p.get_product_id(), "name": p.get_name(), "price": p.get_price(), "stock": p.get_stock()}
        for p in inventory.get_products()
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved to {filename}.")  

import json

INVENTORY_FILE = "inventory.json"


# ======================= Product class =======================
class Product:
    """Represents a single product and manages its own state."""

    def __init__(self, product_id, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = 0
        self.update_stock(stock)  # reuse validation rules

    # Getter methods give read-only access to the private attributes
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


# ======================= Inventory class =======================
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


# ======================= File handling =======================
def load_inventory(filename):
    """Load an Inventory from a JSON file. Returns an empty Inventory on failure."""
    inventory = Inventory()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"{filename} found.")
        for item in data:
            try:
                inventory.add_product(
                    Product(item["id"], item["name"], item["price"], item["stock"])
                )
            except (KeyError, TypeError, ValueError):
                print(f"WARNING: Skipped an invalid product entry: {item}")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty inventory.")
    except json.JSONDecodeError:
        print("ERROR: Could not read inventory file. Starting with an empty inventory.")
    return inventory


def save_inventory(inventory, filename):
    """Save an Inventory to a JSON file."""
    data = [
        {"id": p.get_product_id(), "name": p.get_name(), "price": p.get_price(), "stock": p.get_stock()}
        for p in inventory.get_products()
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved to {filename}.")


# ======================= Main program =======================
def get_valid_int(prompt):
    """Prompt until the user enters a non-negative whole number."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print(f"  ERROR: '{value}' is not a valid non-negative whole number.")


def get_valid_float(prompt):
    """Prompt until the user enters a non-negative number."""
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number < 0:
                print("  ERROR: Price cannot be negative.")
                continue
            return number
        except ValueError:
            print(f"  ERROR: '{value}' is not a valid number.")


def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def add_product_menu(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    if not product_id:
        print("\nERROR: Product ID cannot be empty.")
        return
    if inventory.find_product(product_id):
        print(f"\nERROR: Product ID '{product_id}' already exists.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("\nERROR: Product name cannot be empty.")
        return

    price = get_valid_float("Price: ")
    stock = get_valid_int("Stock Quantity: ")

    inventory.add_product(Product(product_id, name, price, stock))
    print("\nProduct added successfully!")


def update_stock_menu(inventory):
    print("\nUpdate Stock")
    product_id = input("Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is None:
        print(f"\nProduct '{product_id}' not found.")
        return

    print(f"Current stock for {product.get_name()}: {product.get_stock()}")
    product.update_stock(get_valid_int("New Stock Quantity: "))
    print("\nStock updated successfully!")


def search_product_menu(inventory):
    print("\nSearch Product")
    keyword = input("Enter Product ID or Name: ")
    matches = inventory.search_product(keyword)
    if not matches:
        print("\nNo matching product found.")
        return
    inventory.display_products(matches, "Search Results")


print("=" * 41)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 41)
print()

inventory = load_inventory(INVENTORY_FILE)

while True:
    display_menu()
    choice = input("\nEnter option: ").strip()

    if choice == "1":
        inventory.display_all()
    elif choice == "2":
        add_product_menu(inventory)
    elif choice == "3":
        update_stock_menu(inventory)
    elif choice == "4":
        search_product_menu(inventory)
    elif choice == "5":
        save_inventory(inventory, INVENTORY_FILE)
    elif choice == "6":
        print("\nExiting Inventory Management System. Goodbye!")
        break
    else:
        print("\nInvalid option. Please enter a number from 1 to 6.") 