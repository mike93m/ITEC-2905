# Create an empty list to store the names
class_list = []

# While loop to allow for multiple inputs
while True: 
    # Get the naame of the class and add it to the list
    class_name = input('Enter a class name: ')
    # If user inputs nothing, break the loop
    if not class_name:
        break
    class_list.append(class_name) 

# Loop through the list and display the class names
for course in class_list:
    print(course)

                       