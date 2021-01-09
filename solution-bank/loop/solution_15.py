"""
Compute the natural logarithm of 2, by adding up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
where n is a positive integer and input by user.
"""

n = int(input())

result = 0
factor = 1

for i in range(1, n + 1):
    result += factor / i
    factor *= -1

print(result)
