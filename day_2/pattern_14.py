"""
n = 7
*
**
***
****
***
**
*

n = 4
*
**
**
*

# upper triangle (n - n // 2)
# stars: i + 1

# lower triangle (n // 2)
stars: n // 2 - i
"""

n = int(input())

# upper triangle
for i in range(n - n // 2):
    print('*' * (i + 1))

# lower triangle
for i in range(n // 2):
    print('*' * (n // 2 - i))
