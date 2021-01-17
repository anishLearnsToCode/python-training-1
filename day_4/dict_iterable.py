words = {
    'i': 100,
    'am': 100,
    'batman': 12,
    'hello': 560,
    'world': 89
}

# iterate over the keys
# print(words.keys())

# for key in words.keys():
#     print(key in words)

# for key in words:
#     print(key)

"""
key = am
print('i' in words)
True
True
"""

# values
# print(words.values())

# for value in words.values():
#     print(value % 2 == 0)

"""
True
True
True
True
False
"""

# items
# print(words.items())

for key, value in words.items():
    # python unpacking
    print(key, value)
