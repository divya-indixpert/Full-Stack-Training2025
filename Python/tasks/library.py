import datetime 

d = input("Enter date & time (YYYY-MM-DD ): ")
dt = datetime.datetime.strptime(d, "%Y-%m-%d ")

days = int(input("Enter number of days to add: "))

new_date = dt + datetime.timedelta(days=days)

print("New Date & Time:", new_date)
