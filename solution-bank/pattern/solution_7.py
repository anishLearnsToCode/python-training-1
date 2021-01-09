rows = int(input())

for row in range(rows):
    for j in range(row + 1):
        print(j + 1, end=' ')
    print()
