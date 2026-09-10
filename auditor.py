print("=== Inventory Audit System ===")
print("Enter stock quantity for each delivery.")
print("Type 'quit' at any time to stop and see the report.\n")
while True:
        user_input = input("Enter stock quantity: ")

        if user_input.lower() == "quit":
            break
        if not user_input.isdigit():
            print(f"  ERROR: '{user_input}' is not a valid whole number. Entry rejected.\n")
            continue

        quantity = int(user_input)
total_inventory = 0 
