rows = int(input())

# upper triangle
for i in range(rows):
    # spaces
    print(end=' ' * (rows - 1 - i))

    # first star
    print(end='*')

    # spaces
    print(end=' ' * (2 * i - 1))

    # second star
    print('' if i is 0 else '*')

# lower triangle
for i in range(rows - 1):
    # spaces
    print(end=' ' * (i + 1))

    # first star
    print(end='*')

    # spaces
    print(end=' ' * (2 * rows - 5 - 2 * i))

    # second star
    print('' if i is rows - 2 else '*')
