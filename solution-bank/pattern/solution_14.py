rows = int(input())

# upper triangle
for i in range(rows - rows // 2):
    print('*' * (i + 1))

# lower triangle
for i in range(rows // 2):
    print('*' * (rows // 2 - i))
