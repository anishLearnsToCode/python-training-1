# val = 'hello world {1} {0}'.format(12, 3.14)

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""

val = f'hello world {12} {"hello"} {True} {False} {range(1, 10)} {not False} {(1 - 90) ** 2 + 78}'

print(val)
