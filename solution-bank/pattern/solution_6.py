rows = int(input())

for row in range(rows - 1):
    # spaces
    print(' ' * (rows - row - 1), end='')

    # first star
    print('*', end='')

    # spaces
    print(' ' * (2 * row - 1), end='')

    # second star
    print('' if row is 0 else '*')

# last row
print('* ' * rows)
