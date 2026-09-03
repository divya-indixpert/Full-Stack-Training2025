students = {}

while True:
    print("\n1. Register student")
    print("2. Search student record")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        address = input("Enter student address: ")
        email = input("Enter student email: ")

        students[id] = {
            "name": name,
            "address": address,
            "email": email
        }
        print("Student registered successfully ")
    elif choice == "2":
        id = int(input("Enter student ID to search: "))
        if id in students:
            print("Student Found")
            print("Name:", students[id]["name"])
            print("Address:", students[id]["address"])
            print("Email:", students[id]["email"])
        else:
            print("No student found")

    elif choice == "3":
        print("Thank you, program exited ")
        break

    else:
        print("Invalid choice ,  Please try again.")
