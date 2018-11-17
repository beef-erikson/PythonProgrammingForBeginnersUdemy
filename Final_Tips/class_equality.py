"""Example of how to define the equality of classes.
"""


class Student:
    def __init__(self, student_id):
        """Initialization. Sets student_id.
        """
        self.student_id = student_id

    def __eq__(self, other):
        """Checks equality of student_id.
        """
        return self.student_id == other.student_id


# Creates objects
student1 = Student(1)
student2 = Student(2)
student3 = Student(1)
student4 = student1

# True
print(student1 == student4)
# False
print(student1 == student2)
# True - without the equality definition this would normally be false
print(student1 == student3)
