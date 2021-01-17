"""
n
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input())
odd = 0
even = 0

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        even += number
    else:
        odd += number

print(f'Sum of even numbers: {even}')
print(f'Sum of odd numbers: {odd}')
