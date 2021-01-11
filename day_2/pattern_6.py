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

n = int(input())

# main pattern
for i in range(n - 1):
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
