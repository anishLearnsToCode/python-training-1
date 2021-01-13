"""
map(func, iterable)

for item in iterable:
    func(item)
"""


def hello_str(x: str) -> int:
    return len(x)


# result = list(map(len, input().split()))

# print(result)
# print(type(result))


def is_odd(number: int) -> bool:
    return number % 2 == 1


print(list(map(is_odd, [1, 2, 3, 4, 5])))
