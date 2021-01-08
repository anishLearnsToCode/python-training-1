"""
n! = 1 * 2 * 3 * .. * n
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
"""

n = int(input())

factorial = 1

while n > 1:
    factorial = factorial * n
    n = n - 1

print(factorial)
