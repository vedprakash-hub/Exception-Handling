# Custom Exceptions
class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass


# Inventory Data
inventory = {
    101: {"name": "Laptop", "stock": 5},
    102: {"name": "Phone", "stock": 10},
    103: {"name": "Tablet", "stock": 3}
}


while True:
    print("\n--- Inventory Management System ---")
    print("1. View Products")
    print("2. Purchase Product")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            for pid in inventory:
                print(pid, inventory[pid]["name"], "Stock:", inventory[pid]["stock"])

        elif choice == 2:
            try:
                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter quantity: "))

                if pid not in inventory:
                    raise InvalidProductIDError("Product ID does not exist")

                if qty <= 0:
                    raise InvalidQuantityError("Quantity must be greater than 0")

                if inventory[pid]["stock"] < qty:
                    raise OutOfStockError("Not enough stock available")

                inventory[pid]["stock"] -= qty
                print("Purchase successful")

            except (InvalidProductIDError, InvalidQuantityError, OutOfStockError) as e:
                print("Error:", e)

        elif choice == 3:
            print("Exiting system")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")