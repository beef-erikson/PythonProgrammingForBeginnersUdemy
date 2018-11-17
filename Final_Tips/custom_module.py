"""Example of creating a custom module.
"""


# Creates the class and methods to use from import
def method_1():
    print('method 1')


class ClassA:
    @staticmethod
    def class_method_1():
        print('class_method_1 method 1')


print(__name__)

if __name__ == '__main__':
    method_1()
    ClassA.class_method_1()
