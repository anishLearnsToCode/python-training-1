"""
n = 4
 j 0 1 2 3 4
i
0: 1
1: 1 2 1
2: 1 2 3 2 1
3: 1 2 3 4 3 2 1

# increasing
count = i + 1
f(j) = j + 1

j : 0 1 2 3 4 5
s : 1 2 3 4 5 6 7

# decreasing
count = i
f(i, j) = i - j

j : 0 1 2 3 4
i = 3
s : 3 2 1
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):
    # [1 + 2 + 3 + ... n] + [0 + 1 + 2 + 3 + ... + (n - 1)] = O(n^2) + O(n^2) = O(n^2)
    # increasing sequence
    for j in range(i + 1):
        print(j + 1, end=' ')

    # decreasing sequence
    for j in range(i):
        print(i - j, end=' ')

    # new line
    print()
