print("=== Inventory Audit System ===")
print("Enter stock quantity for each delivery.")
print("Type 'quit' at any time to stop and see the report.\n")
while True:
        user_input = input("Enter stock quantity: ")

        if user_input.lower() == "quit":
            break
total_inventory = 0 
