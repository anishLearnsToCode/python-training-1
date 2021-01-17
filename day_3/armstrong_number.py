"""
1
1^3 = 1

153
1^3 + 5^3 + 3^3
1 + 125 + 27 = 153
"""

"""
Time Complexity: O(number)
Space Complexity: O(1)
"""
def is_armstrong(number: int) -> bool:
    sum_cubes = 0
    for digit in str(number):
        sum_cubes += int(digit) ** 3
    return sum_cubes == number


"""
Time Complexity: O(b - a)
Space Complexity: O()
"""
def number_armstrong_numbers(a: int, b: int) -> int:
    # terms = b - a
    # a + (a + 1) + (a + 2) + (a + 3) + .. (b - 2) + (b - 1) + b <= (b + b + b + b + .. + b) (b - a) times
    # b(b - a) = O(b^2 - ab)
    # s(b) - s(a) = O(b^2 - a^2) = O(b^2)
    count = 0
    for i in range(a, b):
        # O(i)
        if is_armstrong(i):
            count += 1
    return count


print(number_armstrong_numbers(100, 200))
