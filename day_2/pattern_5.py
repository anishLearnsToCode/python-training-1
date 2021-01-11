"""
rows = 5
____*
___* *
__* * *
_* * * *
* * * * *

# spaces: n - 1 - i

i : 0 1 2 3 4
s : 4 3 2 1 0


# stars: i + 1

i : 0 1 2 3 4
s : 1 2 3 4 5
"""

n = int(input())

for i in range(n):
    # spaces
    print(end=' ' * (n - 1 - i))

    # stars
    print('* ' * (i + 1))
