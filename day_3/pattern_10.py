"""
n = 4
A
A B A
A B C B A
A B C D C B A

# increasing letters
count: i + 1
f(i, j): chr('A' + j)

# decreasing letters
count: i
f(i, j) = chr('A' + i - 1 - j)
s(0):
s(1): A
s(2): B A
s(3): C B A
v(i, j) = A + i - 1 - j
"""


n = int(input())

for i in range(n):
    # increasing
    for j in range(i + 1):
        print(end=chr(ord('A') + j) + ' ')

    # decreasing
    for j in range(i):
        print(end=f'{chr(ord("A") + i - 1 - j)} ')

    # new line character
    print()
