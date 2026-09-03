students = []
n = int(input("please enter the number you enter student: "))
if n not in [1,2,3,4,5,6]:
    print("wrong value")
else:
    for i in range(n):
        student = {
            "id": int(input("Enter id: ")),
            "name": input("Enter name: "),
            "address": input("Enter address: ")
        }
        students.append(student)
    print("\n All Students Details ")
    for data in students:
        print(data)



 