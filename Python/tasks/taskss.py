import json
n = int(input("How many students you want to register: "))

while n > 5 or n <= 0:
    print("Invalid! Please enter number between 1 to 5.")
    n = int(input("How many students (max 5): "))

count = 1
while count <= n:
    print("\nStudent", count)

    name = input("Enter name: ")
    id = input("Enter ID: ")
    address = input("Enter address: ")

    print("Name:", name)
    print("ID:", id)
    print("Address:", address)

    count += 1


    