def printRow(columns: int) -> None:
    for i in range(columns): print('*', end='')
    print()


rows = int(input())
columns = int(input())

if rows < 2:
    print("invalid")
    exit(0)

printRow(columns)
for i in range(rows - 2):
    print('*', end='')
    for j in range(columns - 2): print(end=' ')
    print('*')

printRow(columns)
