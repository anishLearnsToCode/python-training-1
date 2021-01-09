rows = int(input())

# upper triangle
for i in range(rows):
    # spaces
    print(' ' * (rows - 1 - i), end='')

    # stars
    print('* ' * (i + 1))


# lower triangle
for i in range(rows - 1):
    # spaces
    print(' ' * (i + 1), end='')

    # stars
    print('* ' * (rows - 1 - i))
