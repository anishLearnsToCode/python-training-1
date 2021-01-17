"""
1 is not a prime number
2, 3, 5, 7, 11, 13, 19, 23, 29 ...
non prime = composite
[2, n - 1]

16
1, 16
2, 8
4, 4
8, 2
16, 1

9
1, 9
3, 3
9, 1

25
1, 25
5, 5
25, 1

36
1, 36
2, 18
3, 12
4, 9
6, 6
9, 4
12, 4
18, 2
36, 1

19
0 --> sqrt(19)

d^2 <= n
d <= sqrt(n)
"""
"""
Time Complexity: O(sqrt(number))
Space Complexity: O(1)
"""
def is_prime(number: int) -> bool:
    if number == 1:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def is_prime_linear(number: int) -> bool:
    if number == 1:
        return False
    divisor = 2
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

# 5210644015679228794060694325390955853335898483908056458352183851018372555735221