"""
Time Complexity: O(k1 + k2 + (n - 1) * (k3) + k4) = O()
n * k + k2          O(n)

Space Complexity: O(1)
"""

"""
n! = 1 * 2 * 3 * .. * n
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
"""

n = int(input()) # k1

factorial = 1 # k2

while n > 1: # n - 1
    factorial = factorial * n # k3
    n = n - 1                 # k3

print(factorial)                # k4
