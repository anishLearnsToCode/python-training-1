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

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

n = int(input())

# upper triangle
for i in range(n - n // 2):
    # 1 2 3 4 5 ... (n / 2 - 1) = (n - 1)(n - 3) / 8 = O(n^2)
    print('*' * (i + 1))

# lower triangle
for i in range(n // 2):
    # n / 2 (n / 2 - 1) (n / 2- 2)... 0 = O(n^2)
    print('*' * (n // 2 - i))
