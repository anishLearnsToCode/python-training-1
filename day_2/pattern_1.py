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

rows = int(input())
stars = int(input())

for n in range(rows):
    # printing stars
    # for j in range(stars):
    #     print('*', end='')

    print('*' * stars)

    # sending to the next line
    # print()
