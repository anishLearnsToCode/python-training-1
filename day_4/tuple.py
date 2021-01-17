"""
()
- tuples are immutable
- strings are immutable
- range is immutable
- list is mutable

- tuples are iterable
- tuple slicing
- tuple indexing
"""

# car = ('honda', 'city', 'DL7680', '8787678', 2016)

# print(len(car))
# print(type(car))

# first_name = 'john'

t = (1, 2, 3, 'hello', False, [-9, 78])

t[-1][0] = 0
print(t)
