
students = {
    "101": {
        "name": "Divya",
        "qualification": "B.Com",
        "email": "divya@gmail.com"
    },
    "102": {
        "name": "Amit",
        "qualification": "B.Sc",
        "email": "amit@gmail.com"
    },
    "103": {
        "name": "Neha",
        "qualification": "M.Com",
        "email": "neha@gmail.com"
    }
}
user_id = input("Enter your student ID: ")
if user_id in students:
    print(" Student Found")
    print("Name:", students[user_id]["name"])
    print("Qualification:", students[user_id]["qualification"])
    print("Email:", students[user_id]["email"])
else:
    print(" Invalid ID")