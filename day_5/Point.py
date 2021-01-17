import math

# ADT Abstract Data Type
class Point:
    # methods
    def __init__(self, x: int, y: int):
        # print('hey someone is creating a point object')
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)
        # return 100

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __bool__(self):
        return not (self.x == 0 and self.y == 0)

    def __mul__(self, other):
        return Point(x=self.x * other.x, y=self.y * other.y)

    # def __truediv__(self, other):


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name}.{last_name}@gmail.school.com'
        self.enrolled_classes = []

    def enrollClass(self, class_name: str):
        if class_name in self.enrolled_classes:
            return
        self.enrolled_classes.append(class_name)

    def __repr__(self) -> str:
        return f'Student(first={self.first_name}, last={self.last_name}, classes={self.enrolled_classes})'

    # def __str__(self) -> str:
    #     return f'{self.first_name} {self.last_name} - {self.email}'


# john = Student(last_name='Doe', first_name='John')
# print(repr(john))
#
# john.enrollClass('fencing')
# john.enrollClass('chess')
# john.enrollClass('math')
# john.enrollClass('golf')
#
# print(john)
# john.enrolled_classes = []
# print(john)

p1 = Point(-10, 2)
p2 = Point(8, 3)

print(p1 + p2)

print(bool(p1))
print(bool(p2))
print(bool(Point(0, 0)))

print(p1 * p2)

# p = Point(10, -83)
# print(p)
