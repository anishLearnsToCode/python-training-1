def sumNaturalNumbers(n: int) -> int:
    return n * (n + 1) // 2


rows = int(input())

# upper triangle
number = 1
for i in range(rows):
    for j in range(i + 1):
        print(number if j == i else f'{number}*', end='')
        number += 1
    print()

# lower triangle
for i in range(rows):
    number = sumNaturalNumbers(rows - 1 - i) + 1
    for j in range(rows - i):
        print(number if j == rows - i - 1 else f'{number}*', end='')
        number += 1
    print()
