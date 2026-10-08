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

