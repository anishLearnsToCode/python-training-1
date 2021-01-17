# print(max(1, 2, 3, 4, 5, 100, -2, -2, -10))
# print(min(1, 2, 3, 4, 5, 100, -2, -2, -10))
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

n = int(input())

numbers = [x for x in range(1, n)]
print(numbers)
# print(max(numbers))
# print(min(numbers))

print(sum(numbers))
