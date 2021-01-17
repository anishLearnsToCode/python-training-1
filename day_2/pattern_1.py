"""
Time Complexity: O(rows * stars)
Space Complexity: O(1)
"""

"""
rows = 3

****
****
****

rows = 5

****
****
****
****
****

"""

rows = int(input())         # 4
stars = int(input())        # 10   10 + 10 + 10+ 10 = 40

for n in range(rows):       # rows
    # printing stars
    # for j in range(stars):
    #     print('*', end='')

    # time complexity: O(stars)
    print('*' * stars)

    # sending to the next line
    # print()
