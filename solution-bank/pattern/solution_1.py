rows = int(input())

for i in range(rows):
    for j in range(rows - i): print('*', end='')
    for j in range(2 * i): print(' ', end='')
    for j in range(rows - i): print('*', end='')
    print()

for i in range(rows):
    for j in range(i + 1): print('*', end='')
    for j in range(2 * rows - 2 * i - 2): print(' ', end='')
    for j in range(i + 1): print('*', end='')
    print()
