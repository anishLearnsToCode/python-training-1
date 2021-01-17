"""
1 is not a prime number
2, 3, 5, 7, 11, 13, 19, 23, 29 ...
non prime = composite
[2, n - 1]
"""
def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
