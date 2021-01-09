rows = int(input())

for i in range(rows + 1): print('*', end='\n' if i is rows else '')

for i in range(rows - 1):
    print(end='*')
    for j in range(rows - i - 2): print(end=' ')
    print('' if i == rows - 2 else '*')
