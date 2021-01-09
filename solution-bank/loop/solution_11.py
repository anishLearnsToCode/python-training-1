"""
WAP to enter the numbers till the user wants and at the end the program should display the
largest and smallest numbers entered.
"""

"""
WAP to enter the numbers till the user wants and at the end it should display the count of positive,
negative and zeros entered.
"""

infinity = float('inf')
smallest = infinity
largest = -infinity

while True:
    number = int(input('Number: \t'))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    user_prompt = input('enter another number? (y/n) \t')
    if user_prompt == 'n':
        break

print(f'Smallest Number: {smallest}')
print(f'Largest Number: {largest}')
