#  Student Grade Management System 

students = {}

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student Grade")
    print("2. Update Student Grade")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                sid = int(input("Enter Student ID: "))
                grade = input("Enter Grade: ")

                if grade == "":
                    raise ValueError("Grade cannot be empty")

                students[sid] = grade
                print("Student added successfully")

            except ValueError as e:
                print("Error:", e)

        elif choice == 2:
            try:
                sid = int(input("Enter Student ID to update: "))

                if sid not in students:
                    raise KeyError("Student ID not found")

                grade = input("Enter new Grade: ")

                if grade == "":
                    raise ValueError("Grade cannot be empty")

                students[sid] = grade
                print("Grade updated successfully")

            except KeyError as e:
                print("Error:", e)
            except ValueError as e:
                print("Error:", e)

        elif choice == 3:
            try:
                sid = int(input("Enter Student ID to delete: "))

                if sid not in students:
                    raise KeyError("Student ID not found")

                del students[sid]
                print("Student deleted successfully")

            except KeyError as e:
                print("Error:", e)

        elif choice == 4:
            if len(students) == 0:
                print("No student records found")
            else:
                for i in students:
                    print("ID:", i, "Grade:", students[i])

        elif choice == 5:
            print("Exiting program")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")