"""
n = 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

# increasing numbers
count = n - i

f(i, j) = j + 1

i : 0 1 2 3 4
c : 5 4 3 2 1

# new line
"""
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):          # n + (n - 1) + (n - 2) + 3 + 2 + 1
    # increasing numbers
    for j in range(n - i):
        print(j + 1, end=' ')

    # new line
    print()
