"""
n = 3
1
2*3
4*5*6
4*5*6
2*3
1

n = 4
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1

n = 6
16*17*18*19*20*21
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1

# Upper Triangle (n)
numbers
count : i + 1
constant

# Lower Triangle (n)
count: n - i
f(i, j) = s(n - i - 1) + 1 + j
        = (n - i - 1) (n - i - 1 + 1) / 2 + 1 + j
        = (n - i - 1)(n - i) / 2 + 1 + j

s(n) = 1 + 2 + 3 + 4 + ... + n = n(n + 1) / 2
     = n (n + 1) / 2
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())
k = 1

# upper
for i in range(n):
    for j in range(i + 1):
        if j == i:
            print(k)
        else:
            print(end=f'{k}*')
        k += 1


# lower
for i in range(n):
    for j in range(n - i):
        if j == n - i - 1:
            print((n - i - 1) * (n - i) // 2 + 1 + j)
        else:
            print(end=f'{(n - i - 1) * (n - i) // 2 + 1 + j}*')
