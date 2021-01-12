"""
n = 5
____*
___*_*
__*___*
_*_____*
*_______*
_*_____*
__*___*
___*_*
____*

2nd last row : (n - 2) th
spaces(n - 2) = 2(n - 2) - 1 = 2n - 5

# upper triangle (n)
# spaces: n - i - 1
# star: 1
# spaces: 2i - 1
# star: 1 except for first

# lower triangle (n - 1)
# spaces: i + 1
# star: 1
# spaces: k - 2i
# star: 1 except for last
"""

n = int(input())

# upper triangle
for i in range(n):
    # spaces
    print(end=' ' * (n - 1 - i))

    # star
    print(end='*')

    # spaces
    print(end=' ' * (2 * i - 1))

    # star
    print('' if i == 0 else '*')


# lower triangle
for i in range(n - 1):
    # spaces
    print(end=' ' * (i + 1))

    # star
    print(end='*')

    # spaces
    print(end=' ' * (2 * n - 5 - 2 * i))

    # star
    print('' if i == n - 2 else '*')
