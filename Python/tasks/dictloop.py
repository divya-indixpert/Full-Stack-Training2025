students = []

number = input("Enter number of students: ")


if not number.isdigit():  
    print("Wrong value! Please enter number only.")
elif int(number) > 5: 
    print("You cannot enter more than 5 students.")
else:
    n = int(number)
    for i in range(n):
        print(f"\nEnter details of student {i+1}")
        student = {
            "id": int(input("Enter ID: ")),
            "name": input("Enter Name: "),
            "address": input("Enter Address: ")
        }
        students.append(student)

    print("\n--- All Students Details ---")
    for details in students:
        print(f"ID: { details ['id']}, Name: { details ['name']}, Address: { details ['address']}")
