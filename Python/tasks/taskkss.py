dictdata=[
    {"id":101,"name":"divya","address":"gurgaon"},
    
    {"id":102,"name":"indixpert","address":"Hyderabad"},
    {"id":103,"name":"manisha","address":"UP"}
    ]
name = input("please enter your name:")

for data in dictdata:
    for key, value in data.items():
        if value == name:
            print("record found successfully")
            print(data)
            found = True
            break 
        else:
            print("record does not exist")
            
        
        
