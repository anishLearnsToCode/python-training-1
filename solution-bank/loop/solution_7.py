"""
WAP that reads a set of integers, and then prints the sum of the even and odd integers.
"""

numbers = list(map(int, input().split()))
even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += number
    else:
        odd += number

print(f'Even Sum: {even}')
print(f'Odd Sum: {odd}')
