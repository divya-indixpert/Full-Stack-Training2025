def input_data():
    id = input("enter student id:")
    name = input("enter your name:")
    return id ,  name

def output_data():
    id , name = input_data()
    print("student id:" , id)
    print("student, name:",name)
        
output_data()