TAX_RATE = 0.10  # 10% tax per delivery

def get_valid_input():

    user_input = input("Enter stock quantity: ")

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print(f"  ERROR: '{user_input}' is not a valid whole number. Entry rejected.\n")
        return None

    quantity = int(user_input)

    if quantity < 0:
        print(f"  ERROR: Negative quantity ({quantity}) is not allowed. Entry rejected.\n")
        return None

    return quantity

def process_delivery(current_total, new_value):
    """
    Adds a new delivery amount to the running total.
    Returns the updated total.
    """
    return current_total + new_value

def calculate_tax(amount):
    """
    Calculates the tax owed on a single delivery amount.
    Returns the tax amount (10% of the delivery).
    """
    return amount * TAX_RATE


total_inventory = 0 
failed_entries = 0

print("=== Inventory Audit System ===")
print("Enter stock quantity for each delivery.")
print("Type 'quit' at any time to stop and see the report.\n")

while True:

    result = get_valid_input()

    if result == "quit":
        break

    if result is None:
        failed_entries += 1
        continue

    quantity = result
    total_inventory = process_delivery(total_inventory, quantity)
    tax = calculate_tax(quantity)
    print(f"  Accepted. Delivery: {quantity} units | Tax on this delivery: {tax:.2f}")
    print(f"  Current total inventory: {total_inventory} units.\n")


    if total_inventory > 500:
        print(f"  !! OVERSTOCK ALERT !! Total inventory ({total_inventory}) exceeds 500 units.")
        print("  Halting entry process immediately.\n")
        break
    elif total_inventory == 500:
        print("  Note: Inventory has reached exactly the 500-unit capacity.\n")
    else:
        pass

# This block is now OUTSIDE the loop — runs once, after quit/overstock
print("=== End of Session Report ===")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")