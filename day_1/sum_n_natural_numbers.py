"""
0: 0
1: 1
n: 1 + 2 + 3 + 4 + ... + n
"""

n = int(input())

result = 0
while n > 0:
    result = result + n
    n = n - 1

print(result)


"""
n = 0
result = 0 + 4 + 3 + 2 + 1
4 > 0 ? true
3 > 0 ? true
2 > 0 ? true
1 > 0 ? true
0 > 0 ? false
print(10)
10
"""