a = int(input("please enter first number:"))
b = int(input("plese enter second number:"))

def multiply(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
def menu():
    print("1. multiply")
    print("2. division")
    option = int(input("please select any option:"))
    return option


def dashboard():
    number = menu()
    if number == 1:
        multiply(a,b)
    elif number == 2:
        division(a,b)
        
dashboard()