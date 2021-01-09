rows = int(input())

for i in range(rows):
    # stars
    print('*' * (rows - i), end='')

    # numbers
    print(f'{i + 1}*' * (i + 1), end='')

    # stars
    print('*' * (rows - i - 1))
