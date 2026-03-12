accounts = {
    101: 5000,
    102: 3000,
    103: 7000
}

import time

while True:
    print("\n--- Bank Transaction System ---")
    print("1. Transfer Money")
    print("2. View Accounts")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            try:
                sender = int(input("Enter sender account number: "))
                receiver = int(input("Enter receiver account number: "))
                amount = float(input("Enter amount: "))

                if sender not in accounts or receiver not in accounts:
                    raise KeyError("Incorrect account number")

                if accounts[sender] < amount:
                    raise ValueError("Overdraft! Not enough balance")

                print("Processing transaction...")
                time.sleep(2)

                if amount > 10000:
                    raise TimeoutError("Transaction timeout")

                accounts[sender] -= amount
                accounts[receiver] += amount

                print("Transaction successful")

            except KeyError as e:
                print("Error:", e)

            except ValueError as e:
                print("Error:", e)

            except TimeoutError as e:
                print("Error:", e)

        elif choice == 2:
            for acc in accounts:
                print("Account:", acc, "Balance:", accounts[acc])

        elif choice == 3:
            print("Exiting system")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")