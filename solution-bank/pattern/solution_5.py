rows = int(input())

for i in range(rows):
    # spaces
    print(' ' * (rows - 1 - i), end='')

    # stars
    print('* ' * (i + 1))
