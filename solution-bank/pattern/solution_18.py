# pascal's triangle

from math import factorial


def permutation(n, r) -> int:
    return factorial(n) // factorial(n - r)


def combination(n: int, r: int) -> int:
    return permutation(n, r) // factorial(r)


rows = int(input())

for i in range(rows):
    for j in range(i + 1):
        print(combination(i, j), end=' ')
    print()
