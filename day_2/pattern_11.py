"""
n = 8
********(1*)******* 8
*******(2*)(2*)****** 7
******(3*)(3*)(3*)***** 6
*****4*4*4*4***** 5
****5*5*5*5*5**** 4
***6*6*6*6*6*6*** 3
**7*7*7*7*7*7*7** 2
*8*8*8*8*8*8*8*8* 1

# stars: n - i

# numbers (x*) x= i + 1
count = i + 1

# stars : n - i - 1
i : 0 1 2 3 4 5 6 7
s : 7 6 5 4 3 2 1 0
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

for i in range(n):
    # 2n - i [2n + (2n - 1) + (2n - 2) + (2n - 3) + ... 2n] = O(n^2)
    # stars
    print(end='*' * (n - i))

    # numbers
    print(end=f'{i + 1}*' * (i + 1))

    # stars
    print('*' * (n - i - 1))
