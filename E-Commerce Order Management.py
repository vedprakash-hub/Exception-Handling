products = {
    "Laptop": {"price": 50000, "stock": 5},
    "Phone": {"price": 20000, "stock": 10},
    "Headphones": {"price": 2000, "stock": 8}
}

orders = {}
valid_coupon = "SAVE10"
payments = ["card", "upi", "cash"]

while True:
    print("\n--- Order Management System ---")
    print("1. Place Order")
    print("2. Return Order")
    print("3. View Orders")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            try:
                item = input("Enter product name: ")

                if item not in products:
                    raise KeyError("Product not available")

                if products[item]["stock"] <= 0:
                    raise ValueError("Out of stock")

                qty = int(input("Enter quantity: "))
                payment = input("Enter payment method (card/upi/cash): ")

                if payment not in payments:
                    raise ValueError("Invalid payment method")

                coupon = input("Enter coupon code (or press enter): ")

                price = products[item]["price"] * qty

                if coupon != "":
                    if coupon != valid_coupon:
                        raise ValueError("Invalid coupon code")
                    else:
                        price = price * 0.9   # 10% discount

                products[item]["stock"] -= qty
                orders[item] = price

                print("Order placed successfully")
                print("Total amount:", price)

            except (KeyError, ValueError) as e:
                print("Error:", e)

        elif choice == 2:
            try:
                item = input("Enter product to return: ")

                if item not in orders:
                    raise KeyError("Order not found")

                refund = orders[item]
                del orders[item]
                products[item]["stock"] += 1

                print("Return successful")
                print("Refund amount:", refund)

            except KeyError as e:
                print("Error:", e)

        elif choice == 3:
            if len(orders) == 0:
                print("No orders found")
            else:
                for i in orders:
                    print("Product:", i, "Amount:", orders[i])

        elif choice == 4:
            print("Exiting system")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")