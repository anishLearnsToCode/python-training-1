"""
1 2 3 4 100 -90 45
[1, 2, 3, 4, 100, -90, 45]
"""

numbers = input()
numbers = numbers.split()
print(numbers)

numbers = [int(i) for i in numbers]

print(numbers)
print(type(numbers))
