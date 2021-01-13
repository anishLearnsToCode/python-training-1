"""
{x + 3 | x in (0, 10)}`= {3, 4, 5, ... 13}

{f(x) | for x in range}
"""

# numbers = [float(f'{i / 3 :.1f}') for i in range(1, 31)]
# print(type(numbers))
# print(numbers)

letters = [ord(character) for character in 'hello world']
print(letters)

letters = []
for character in 'hello world':
    letters.append(ord(character))
print(letters)
