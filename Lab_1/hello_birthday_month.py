name = input("Please enter your name: ")
birthday_month = input("Please enter your birth month: ")

name_length = len(name)

print(f"Hello, {name}! Your name has {name_length} letters")

if birthday_month.lower() == "august":
    print("Your birthday was this month!")
else:
    print("Your birthday was noth this month")
