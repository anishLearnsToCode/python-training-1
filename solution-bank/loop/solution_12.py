"""
WAP to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is
equal to the number itself, then the number is called an Armstrong number. For example,
153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )
"""


def isArmstrongNumber(number: int) -> bool:
    return sum(int(digit) ** 3 for digit in str(number)) == number


for i in range(1, 501):
    if isArmstrongNumber(i):
        print(i)
