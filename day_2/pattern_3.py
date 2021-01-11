"""
rows = 4

*****
*__*  0 (1, 2, 1)
*_*   1 (1, 1, 1)
*


star: 1
spaces:

i : 0 1
s : 2 1
n = 4

f(n, i) = n - 2 - i

star: 1

"""

n = int(input())

# first row
print('*' * (n + 1))

# main pattern
for i in range(n - 1):
    # star
    print(end='*')

    # spaces
    print(' ' * (n - 2 - i), end='')

    # star
    print('' if i == n - 2 else '*')
