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
n = int(input())

for i in range(n):
    # increasing numbers
    for j in range(n - i):
        print(j + 1, end=' ')

    # new line
    print()
