inventory = 0
failed_entries = 0
while True:
    user_input = input("Enter stock quantity: ")
    if user_input.lower() == "quit":
        break
    if not user_input.isdigit():
        print(f"  ERROR: '{user_input}' is not a valid whole number. Entry rejected.\n")
        failed_entries += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print(f"  ERROR: Negative quantity ({quantity}) is not allowed. Entry rejected.\n")
        failed_entries += 1
        continue
    elif quantity >= 500:
        print(f"  ERROR: Quantity ({quantity}) exceeds maximum limit (500). Entry rejected.\n")
        break
    elif inventory + quantity > 500:
        print(f"  ERROR: Total Inventory ({inventory + quantity}) exceeds maximum limit (500). Entry rejected.\n")
        break
    elif inventory + quantity == 500:
        print(f"  WARNING: Total Inventory ({inventory + quantity}) currently at maximum capacity. Please quit now.\n")

    inventory += quantity
    print(f"  Accepted. Current total inventory: {inventory} units.\n")
print("=== End of Session Report ===")
print(f"Total inventory: {inventory}")
print(f"Failed entries: {failed_entries}\n")
