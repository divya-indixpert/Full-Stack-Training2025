from registration import students

def search_student():
    search_id = input("enter id to search: ")

    for name in students:
        if name["id"] == search_id:
            print("<<<<<Student Found....:")
            print(name)
           
        else:print("Student not found")
    
    
search_student()
    