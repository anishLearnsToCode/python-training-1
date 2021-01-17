from typing import List

"""
s: no of students
n: no. of subjects (len of marks)
Time Complexity: O(n (s + 1)) = O(s * n)
Space Complexity: O(s * n)
"""
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def average(marks: List[float]) -> float:
    return sum(marks) / len(marks)


students = int(input())
student_marks = {}
for _ in range(students):       # O(s * n)
    # n
    name, *marks = input().split()
    marks = list(map(float, marks))
    student_marks[name] = marks

student_name = input()

# O(n)
result = average(student_marks[student_name])
print(f'{result:.2f}')
