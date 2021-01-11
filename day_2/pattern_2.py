rows = int(input())
columns = int(input())

# first row
print('*' * columns)

# middle section
for i in range(rows - 2):
    # star
    print(end='*')

    # spaces
    print(end=' ' * (columns - 2))

    # star
    print('*')

# last row
print('*' * columns)
