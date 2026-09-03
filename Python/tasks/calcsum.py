def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    choice = input("Enter your choice : ")

    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    if choice == "1":
        print( a + b)

    elif choice == "2":
        print(a - b)
        
    elif choice == "3":
        print(a* b)
    
    else:
        print("invalid choice")
        
calculator()
        
    



