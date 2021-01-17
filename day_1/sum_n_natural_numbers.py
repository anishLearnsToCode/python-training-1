"""
Time Complexity: O(1)
k1 +k1 + n (k2 + k2) + k3 ==> n * K + a = O(n)
Space Complexity: O(1)
"""

"""
0: 0
1: 1
n: 1 + 2 + 3 + 4 + ... + n
"""

n = int(input())            # k1

result = 0                  # k1
while n > 0:                # n
    result = result + n     # k2
    n = n - 1               # k2

print(result)               # k3


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