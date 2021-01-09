rows = int(input())

# upper triangle
for i in range(rows + 1):
    # numbers
    print(f'{rows + i}' * (i + 1))


# lower triangle
for i in range(rows):
    # numbers
    print(f'{2 * rows - 1 - i}' * (rows - i))
