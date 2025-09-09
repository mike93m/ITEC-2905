# Student dataclass
class Student:
    # Each student gets a name and a school ID and a GPA
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    # String representation of the student
    def __str__(self):
        return f'Student Name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}'

#  Sample students 
alex = Student('Alex', 'abc123', 3.8)
print(alex)

sam = Student('Sam', 'xyz789', 3.5)
print(sam)

george = Student('George', 'def456', 3.9)
print(george)

sarah = Student('Sarah', 'HRJ876', 4.0)
print(sarah)