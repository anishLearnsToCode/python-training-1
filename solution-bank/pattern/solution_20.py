# Butterfly Pattern

rows = int(input())

# upper portion
for i in range(rows):
    # stars
    print(end='*' * (i + 1))

    # spaces
    print(end=' ' * (2 * rows - 2 * i - 2))

    # stars
    print('*' * (i + 1))


# lower portion
for i in range(rows):
    # stars
    print(end='*' * (rows - i))

    # spaces
    print(end=' ' * (2 * i))

    # stars
    print('*' * (rows - i))
