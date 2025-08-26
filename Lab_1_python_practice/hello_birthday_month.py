# Get the user's name and birthday month
name = input("Please enter your name: ")
birthday_month = input("Please enter your birth month: ")

# Get the length of the user's name
name_length = len(name)

# Display the results
print(f"Hello, {name}! Your name has {name_length} letters")

# Check if the birthday month is August and display the appropriate message
if birthday_month.lower() == "august":
    print("Your birthday was this month!")
else:
    print("Your birthday was not this month.")
