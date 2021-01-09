rows = int(input())

for row in range(rows - 1):
    # first number
    print(1, end=' ')

    # xxxxx
    print('x ' * (row - 1), end='')

    # second number
    print(row + 1 if row is not 0 else '')

# last row
for i in range(rows):
    print(i + 1, end=' ')
