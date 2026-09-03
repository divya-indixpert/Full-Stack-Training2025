students = []
def register_student():
    id = int(input("enter your id:"))
    name = input("enter your name:")
    address = input("enter your address:")
    
    
    students.append({
       "id" : id,
       "name": name,
       "address": address
    })
    print("student registered successfully:")
    
    
def view_student():
    if students:
         print("Student Found")
         for detail in students:
            print("Name:", detail["name"])
            print("Address:", detail["address"])
    else:
        print("no student record")
    
def search_student_record():
  
    new_id = int(input("enter a id you want to search:"))
    for id in students:
        if new_id==id['id']:
             print("student found")
             print("name:" , id["name"])
             print("address:", id["address"])
        else:
            print("no record found")
            
def exit():
    print("program existed")
    
    
def menu():
    while True:
        print("\n1 . Student registration:")
        print("2. View student data")
        print("3. serach student data")
        print("4. exit")
        
        choice = input("enter choice:")
        if choice == "1":
            register_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student_record()
        elif choice == "4":
            print("exit")
            break
        else:
            print("invalid choice")
            
            
menu()
    
    
    
