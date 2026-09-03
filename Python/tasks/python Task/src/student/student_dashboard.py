students = []
def add_student():
    name = input("enter your name:")
    id = int(input("enter your id"))
    address = input("enter your address:")
    students.append({"id": id , "name" : name})
    print("student added successfully:")
    
def view_student():
    for s in students:
        print(s)
        
    
    
def delete_student():
    id = input("enter your id you want to delete:")
    if id in students:
        students.remove(id)
        print("students removed")
        
def update_student():
    id= input("enter a id you want to update:")
    for s in students:
        if id == "id":
            new_id= input("enter a id you want to update:")
            s["id"] = "new_id"
            print("student update sucessfully:")
        
            

        