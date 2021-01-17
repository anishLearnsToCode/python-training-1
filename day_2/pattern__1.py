"""
n = 4
******** 0 (4 0 4) 0
***  *** 1 (3 2 3) 2
**    ** 2 (2 4 2)
*      * 3 (1 6 1)

*      * 0 (1, 6, 1)
**    ** 1 (2, 4, 2)
***  *** 2 (3, 2, 3)
******** 3 (4, 0, 4)

n = 2
**** 0 (2, 0, 2)
*  * 1 (1, 2, 1)

stars: 1 2 3 4
i :    0 1 2 3
f(i) = i + 1

s: 6 4 2 0
i: 0 1 2 3
n = 4

spaces f(n, i) = 2n - 2 - 2i
stars = f(i) = i + 1
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):
    # stars
    print('*' * (n - i), end='')

    # spaces
    print(' ' * 2 * i, end='')

    # stars
    print('*' * (n - i))


for i in range(n):
    # stars
    print('*' * (i + 1), end='')

    # spaces
    print(' ' * (2 * n - 2 - 2 * i), end='')

    # stars
    print('*' * (i + 1))
