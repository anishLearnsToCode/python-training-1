def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def permutation(n: int, r: int) -> int:
    """nPr: n! / (n - r)!"""
    return factorial(n) // factorial(n - r)
    # return factorial(4) // factorial(4 - 2)
    # return 24 // factorial(4 - 2)
    # return 24 // factorial(2)
    # return 24 // 2
    # return 12


def combination(n: int, r: int) -> int:
    """nCr = nPr / r! """
    return permutation(n, r) // factorial(r)


# print(combination(5, 0))
# print(combination(5, 1))
# print(combination(5, 2))
# print(combination(5, 3))
# print(combination(5, 4))
# print(combination(5, 5))

# n = int(input())
# for i in range(n + 1):
#     print(combination(n, i))