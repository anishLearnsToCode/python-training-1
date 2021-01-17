from typing import List


def average(marks: List[float]) -> float:
    return sum(marks) / len(marks)


students = int(input())
student_marks = {}
for _ in range(students):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student_marks[name] = marks

student_name = input()

result = average(student_marks[student_name])
print(f'{result:.2f}')
