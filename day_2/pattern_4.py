"""
rows = 5
* * * * * 0 0
_* * * *  1 1
__* * *   2 2
___* *    3 3
____*     4 4

# spaces: i
# stars (*_): n - i

i : 0 1 2 3 4
p : 5 4 3 2 1
f(n,i) = n - i
n n-1 n-2 .. n-n
5 4 3 2 1 0 -1 -2
"""

n = int(input())

for i in range(n):
    # spaces
    print(' ' * i, end='')

    # stars
    print('* ' * (n - i))
