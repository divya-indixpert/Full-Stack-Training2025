students=[]

def add_student():
    id = input("enter your id: ")
    name = input("enter your name: ")
    address = input("enter your address: ")

    student = {
        "id": id,
        "name": name,
        "address": address
    }

    students.append(student)
    print("student registered successfully")
    
    
add_student()