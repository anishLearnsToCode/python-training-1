rows = int(input())

for i in range(rows):
    # increasing
    for j in range(i + 1):
        print(chr(ord('A') + j), end=' ')

    # decreasing
    for j in range(i):
        print(chr(ord('A') - 1 + i - j), end=' ')

    # new line
    print()
