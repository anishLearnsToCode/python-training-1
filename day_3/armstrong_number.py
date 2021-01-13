"""
1
1^3 = 1

153
1^3 + 5^3 + 3^3
1 + 125 + 27 = 153
"""


def is_armstrong(number: int) -> bool:
    sum_cubes = 0
    for digit in str(number):
        sum_cubes += int(digit) ** 3
    return sum_cubes == number


def number_armstrong_numbers(a: int, b: int) -> int:
    count = 0
    for i in range(a, b):
        if is_armstrong(i):
            count += 1
    return count


print(number_armstrong_numbers(100, 200))
