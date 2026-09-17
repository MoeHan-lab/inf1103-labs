total_inventory = 0 
failed_entries = 0

print("=== Inventory Audit System ===")
print("Enter stock quantity for each delivery.")
print("Type 'quit' at any time to stop and see the report.\n")

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

    total_inventory += quantity
    print(f"  Accepted. Current total inventory: {total_inventory} units.\n")

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