"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
n: 1^2  + 2^2  + 3^2 + ... + n^2
"""

n = int(input())

result = 0
i = 1

while i <= n:
    result = result + i ** 2
    i = i + 1

print(result)

"""
n = 1
result = 0 + 1
i = 2
1 <= 1 ? true
2 <= 1 ? false
"""
