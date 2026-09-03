from src.student.student_dashboard import add_student,view_student,delete_student,update_student
   
def student_detail():
    while  True:
        print("****Here are the Menu of the Registration:****")
        print("add student")
        print("view student")
        print("delete student")
        print("update student")
        user_detail()
    
def user_detail():    
    choice = int(input("enter your choice:"))

    if choice == 1:
        add_student()
    
    elif choice == 2:
         view_student()
    
    elif choice == 3:
        delete_student()
    
    elif choice == 4:
        update_student()
        