"""
{x + 3 | x in (0, 10)}`= {3, 4, 5, ... 13}

{f(x) | for x in range}
"""

# numbers = [float(f'{i / 3 :.1f}') for i in range(1, 31)]
# print(type(numbers))
# print(numbers)

"""
Time Complexity: O(n)
Space Complexity: O(n)
n = len(string)
"""

string = input()

letters = [ord(character) for character in string]
print(letters)

letters = []
for character in string:
    letters.append(ord(character))
print(letters)
