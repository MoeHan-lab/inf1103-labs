import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    """Load inventory from inventory.json if it exists, else return an empty list."""
    try:
        with open(INVENTORY_FILE, "r") as f:
            inventory = json.load(f)
        print(f"{INVENTORY_FILE} found.")
        print("Inventory loaded successfully.")
        return inventory
    except FileNotFoundError:
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return []
    except json.JSONDecodeError:
        print("ERROR: Could not read inventory file. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    """Save the inventory list to inventory.json."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f"Inventory saved to {INVENTORY_FILE}.")

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

def find_product(inventory, product_id):
    """Return the product dict matching product_id (case-insensitive), or None."""
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None


def display_all(inventory):
    """Display every product in the inventory."""
    print("\nCurrent Inventory")
    print("-" * 47)
    if not inventory:
        print("Inventory is empty.")
    else:
        for p in inventory:
            print(f"ID: {p['id']} | Name: {p['name']} | "
                  f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 47)

def add_product(inventory):
    """Add a new product to the inventory."""
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()

    if not product_id:
        print("\nERROR: Product ID cannot be empty.")
        return
    if find_product(inventory, product_id):
        print(f"\nERROR: Product ID '{product_id}' already exists.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("\nERROR: Product name cannot be empty.")
        return

    price = get_valid_float("Price: ")
    stock = get_valid_int("Stock Quantity: ")

    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })
    print("\nProduct added successfully!")

