hindi = int(input("enter hindi marks"))
english = int(input("enter english marks"))
maths = int(input("enter maths marks"))
accounts =int(input("enter accounts marks"))
total = hindi + english + maths+ accounts
percentage = total/4

if percentage >= 80:
    print("grade A")
elif percentage >= 70:
    print("grade B")
elif percentage >= 60:
    print("grade C")
else:
    print("fail")
