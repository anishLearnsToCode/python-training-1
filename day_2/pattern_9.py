"""
n = 6
1
1 2
1 x 3
1 x x 4
1 x x x 5
1 2 3 4 5 6

# main pattern
# 1

# x: i - 1

i : 0 1 2 3 4
x : -1 0  1 2 3 ....

# number: i + 1 except for 0th row

# last row
# increasing numbers
n
f(i) = i + 1
0 1 2 3 4 5
1 2 3 4 5 6
"""

n = int(input())

# main pattern
for i in range(n - 1):
    # 1
    print(end='1 ')

    # x
    print(end='x ' * (i - 1))

    # number
    print('' if i == 0 else i + 1)

# last row
for i in range(n):
    print(i + 1, end=' ')
