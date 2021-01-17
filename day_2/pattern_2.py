"""
Time Complexity: O(rows * columns)
Space Complexity: O(1)
"""


rows = int(input())
columns = int(input())

# first row
# time: O(columns)
print('*' * columns)

# middle section
for i in range(rows - 2):       # O(columns * (rows - 2)) = O(rows * columns)
    # star
    # time: O(1)
    print(end='*')

    # spaces
    # O(columns)
    print(end=' ' * (columns - 2))

    # star
    # O(1)
    print('*')

# last row
# time: O(columns)
print('*' * columns)
