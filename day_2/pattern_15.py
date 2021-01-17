"""
n = 3
3
44
555
6666
555
44
3

n = 2

2
33
444
33
2

# upper triangle (n + 1)
count = i + 1
f(i) = n + i

# Lower triangle (n)
count = n - i
f(i, j) = 2n - i - 1
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

# upper triangle
for i in range(n + 1):
    # 1 2 3 4 5 ... n = O(n^2)
    print(f'{n + i}' * (i + 1))

# lower triangle
for i in range(n):
    # n (n - 1) + (n - 2) + 3 + 2 + 1 = O(n^2)
    print(f'{2 * n - 1 - i}' * (n - i))
