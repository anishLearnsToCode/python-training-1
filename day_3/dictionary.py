"""
Dictionary / HashMap / Map / HashTable

list
index --> value
int ----> anything
unique    not unique

key ---> value
anything anything
unique   not unique

- mutable
- iterable

- no booleans
- no lists
- no dict
"""

words = {
    'hello': 100,
    'world': 56,
    'i': 567,
    'am': 100,
    'batman': 34,
    True: 'answer',
    1: 'not answer'
}

# key exists in dictionary
# print('batman' in words)

# accessing elements in dictionary
print(words[True])
# print(words.get('hell', [1, 2, 3, 4]))

# update the value of
