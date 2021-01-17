"""
rows = 5
____*
___*_*
__*___*
_*_____*
* * * * *

10
         *
        *_*
       *___*
      *_____*
     *_______*
    *_________*
   *___________*
  *             *
 *               *
* * * * * * * * * *

# main pattern
# spaces: n - 1 - i
i : 0 1 2 3
s : 4 3 2 1

# star: 1

# spaces: 2i - 1
i : 0 1 2 3 4
s : -1 1 3 5

# star: 1 except for first row


# last row
star: n
"""

"""
Time Complexity: O(n^2)
Space Complexity: O()
"""

n = int(input())

# main pattern
for i in range(n - 1):          # [n + (n - 1) + (n - 2) + (n - 3) + 3 + 2 + 1] + [0 + 1 + 3 + 5 + 7 + .. + 2n - 1] = n(n + 1) / 2 + n^2 = O(n^2)
    # n + (n + 1) + (n + 2) + .. (2n - 1) + 2n = s(2n) - s(n) 4n^2 - n^2 = 3n^2 = O(n^2)
    # n - 1 - i + 2i - 1 = n + i
    # spaces
    print(' ' * (n - 1 - i), end='')

    # star
    print(end='*')

    # spaces
    print(end=' ' * (2 * i - 1))

    # star
    print('' if i == 0 else '*')

# last row
print('* ' * n)
