"""Demonstration of using a list with a class.
"""


class Student:
    def __init__(self, name: str, list_of_marks: list):
        """Initialization.
        """
        self.name = name
        self.list_of_marks = list_of_marks

    def get_number_of_marks(self) -> int:
        return len(self.list_of_marks)

    def get_total_sum_of_marks(self) -> int:
        return sum(self.list_of_marks)

    def get_minimum_mark(self) -> int:
        return min(self.list_of_marks)

    def get_maximum_mark(self) -> int:
        return max(self.list_of_marks)

    def get_mark_average(self) -> float:
        return sum(self.list_of_marks)/len(self.list_of_marks)

    def add_new_mark(self, mark_score: int) -> None:
        self.list_of_marks.append(mark_score)

    def remove_mark_at_index(self, index: int) -> None:
        self.list_of_marks.pop(index)


# Makes new list, creates new student, and uses all class methods
marks = [55, 75, 45, 77, 32, 86]
beef = Student('Beef', marks)
print(f'Number of marks: {beef.get_number_of_marks()}')
print(f'Sum of marks: {beef.get_total_sum_of_marks()}')
print(f'Maximum mark: {beef.get_maximum_mark()}')
print(f'Minimum mark: {beef.get_minimum_mark()}')
print(f'Average: {beef.get_mark_average()}')

beef.add_new_mark(34)
beef.remove_mark_at_index(2)
print(marks)
