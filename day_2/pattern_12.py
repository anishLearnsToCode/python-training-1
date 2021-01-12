"""
n = 3
___*
__* *
_* * *
__* *
___*

# upper triangle
n
# spaces: n - i
# stars(*_): i + 1

# lower triangle
# spaces: i + 2
# stars(*_): n - i - 1

n - 1
"""

n = int(input())

# upper triangle
for i in range(n):
    # spaces
    print(end=' ' * (n - i))

    # stars
    print('* ' * (i + 1))

# lower triangle
for i in range(n - 1):
    # spaces
    print(end=' ' * (i + 2))

    # stars
    print('* ' * (n - 1 - i))
