"""
WAP to enter the numbers till the user wants and at the end it should display the count of positive,
negative and zeros entered.
"""

zeros = 0
negative = 0
positive = 0

while True:
    number = int(input('Number: \t'))
    if number == 0:
        zeros += 1
    elif number > 0:
        positive += 1
    else:
        negative += 1
    user_prompt = input('enter another number? (y/n) \t')
    if user_prompt == 'n':
        break

print(f'No. of Zeros: {zeros}')
print(f'No. of Positive Numbers: {positive}')
print(f'No. of Negative Numbers: {negative}')
