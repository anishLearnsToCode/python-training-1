"""
WAP that prompts the user to input a positive integer. It should then output a message
indicating whether the number is a prime number.
"""

number = int(input())
is_prime = True

for i in range(2, number):
    if number % i == 0:
        print('composite number')
        is_prime = False
        break

if is_prime and number is not 1:
    print('prime number')
