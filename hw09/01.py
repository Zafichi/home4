import typing
from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    name: str = field(compare=False)
    average_mark: float
    subjects: typing.List[str] = field(default_factory=list, repr=False, compare=False)
    age: int = field(default=18, repr=False, compare=False)

    def __post_init__(self):
        if self.name is not None:
            self.first_letter = self.name[0]
        else:
            self.first_letter = None

    def sorted_students(self, *args):
        lst_of_students = [self]
        for i in args:
            lst_of_students.append(i)
        lst_of_students.sort()
        return lst_of_students


student_1 = Student('Alex', 7.56, ['Math', 'PE', 'Chemical'], 21)
student_2 = Student('Patric', 8.88, ['English', 'PE', 'Chemical'])
student_3 = Student('Kate', 9.23, ['Math', 'PE', 'OBJ'], 20)
student_4 = Student('Ann', 10.0, ['English', 'Chemical'], 17)
student_5 = Student('Lukas', 9.23, ['Math', 'PE', 'Economics'], 21)
student_6 = Student('Iron', 6.66, ['Geography', 'PE', 'Chemical'], 22)
print(student_1)
print(student_2 < student_1)
print(student_1.sorted_students(student_2, student_3, student_4, student_5, student_6))
