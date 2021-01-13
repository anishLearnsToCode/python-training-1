"""
n = 3
*____* 4
**__** 2
****** 0
******
**  **
*    *

n = 5
*________* 8
**      **
***    ***
****  ****
**********
********** 0
****  **** 2
***    *** 4
**      ** 6
*        * 8

Upper
stars: i + 1
spaces: 2n - 2 - 2i
stars: i + 1

Lower
stars: n - i
spaces: 2i
stars: n - i
"""

n = int(input())

for i in range(n):
    print(end='*' * (i + 1))
    print(end=' ' * (2 * n - 2 - 2 * i))
    print('*' * (i + 1))

for i in range(n):
    print(end='*' * (n - i))
    print(end=' ' * 2 * i)
    print('*' * (n - i))
