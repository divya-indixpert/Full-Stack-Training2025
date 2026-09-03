import json
student_detail=[]
for i in range(1,7):
    student = {}
    student["id"] = input("Enter student ID: ")
    student["name"] = input("Enter student Name: ")
    student_detail.append(student)

    
        
print(json.dumps(student_detail, indent= 4)) 