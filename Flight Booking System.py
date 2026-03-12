class SeatNotAvailableError(Exception):
    pass

class InvalidPassengerError(Exception):
    pass

class PaymentFailureError(Exception):
    pass


flights = {
    "AI101": {"destination": "Delhi", "seats": 3},
    "AI202": {"destination": "Mumbai", "seats": 2},
    "AI303": {"destination": "Bangalore", "seats": 4}
}

bookings = {}

while True:
    print("\n--- Flight Booking System ---")
    print("1. Search Flights")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("\nAvailable Flights:")
            for f in flights:
                print(f, "Destination:", flights[f]["destination"],
                      "Seats:", flights[f]["seats"])

        elif choice == 2:
            try:
                flight_id = input("Enter Flight ID: ")
                name = input("Enter Passenger Name: ")

                if name == "":
                    raise InvalidPassengerError("Passenger details invalid")

                if flight_id not in flights:
                    raise InvalidPassengerError("Invalid flight ID")

                if flights[flight_id]["seats"] <= 0:
                    raise SeatNotAvailableError("Seat not available")

                payment = input("Enter payment status (success/fail): ")

                if payment != "success":
                    raise PaymentFailureError("Payment failed")

                flights[flight_id]["seats"] -= 1
                bookings[name] = flight_id

                print("Ticket booked successfully")

            except (SeatNotAvailableError, InvalidPassengerError,
                    PaymentFailureError) as e:
                print("Error:", e)

        elif choice == 3:
            name = input("Enter passenger name to cancel ticket: ")

            if name in bookings:
                flight_id = bookings[name]
                flights[flight_id]["seats"] += 1
                del bookings[name]
                print("Ticket cancelled successfully")
            else:
                print("Booking not found")

        elif choice == 4:
            print("Exiting system")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")