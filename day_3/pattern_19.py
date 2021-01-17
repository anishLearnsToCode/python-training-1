"""
n = 3
******
**  **
*    *
*    *
**  **
******

n = 5
********** 5 0 5
****  **** 4 2 4
***    *** 3 4 3
**      ** 2 6 2
*        * 1 8 1
*        * 1 8
**      ** 2 6
***    *** 3 4
**** ***** 4 2
********** 5 0

upper rhombus (n)
stars: n - i
spaces: 2 * i
stars: n - i

lower rhombus (n)
stars: i + 1
spaces: 2 (n - 1 - i)
stars: i + 1
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):
    # stars
    print(f'{"*" * (n - i)}{" " * 2 * i}{"*" * (n - i)}')

    # spaces
    # print(end=' ' * 2 * i)

    # stars
    # print('*' * (n - i))

# lower rhombus
for i in range(n):
    print(end='*' * (i + 1))
    print(end=' ' * (2 * n - 2 - 2 * i))
    print('*' * (i + 1))
