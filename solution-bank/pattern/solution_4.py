rows = int(input())

for i in range(rows):
    # spaces
    print(' ' * i, end='')

    # stars
    print('* ' * (rows - i))
