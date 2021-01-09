rows = int(input())

for row in range(rows):
    for j in range(rows - row):
        print(j + 1, end=' ')
    print()
