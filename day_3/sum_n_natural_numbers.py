"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
def sum_n_natural_numbers(n: int) -> int:
    """"n: 1 + 2 + 3 + ... + n"""
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


print(sum_n_natural_numbers(10))
print(sum_n_natural_numbers(3))
print(sum_n_natural_numbers(0))
print(sum_n_natural_numbers(5))
print(sum_n_natural_numbers(4))
