rows = int(input())

print('*' * (rows + 1))

for i in range(rows - 1):
    print(end='*')
    print(' ' * (rows - i - 2), end='')
    print('' if i == rows - 2 else '*')
