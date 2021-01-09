"""
WAP to calculate the sum of following series where n is input by user. 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... 1/n
"""

n = int(input())

result = 0
for i in range(1, n + 1):
    result += 1 / i

print(result)
