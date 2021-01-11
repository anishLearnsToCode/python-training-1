"""
n = 5
   0 1 2 3 4
0: 1
1: 1 2
2: 1 2 3
3: 1 2 3 4
4: 1 2 3 4 5

# increasing numbers
count = i + 1

i j
f(i, j) = j + 1

# new line
"""

n = int(input())

for i in range(n):
    # increasing numbers
    for j in range(i + 1):
        print(j + 1, end=' ')

    # new line
    print()
