"""
WAP a loop that asks the user to enter two numbers. The numbers should be added and the sum displayed.
The loop should ask the user whether he or she wishes to perform the operation again. If so, the loop should repeat;
otherwise it should terminate.
"""

while True:
    a = int(input('Number 1:\t'))
    b = int(input('Number 2:\t'))
    print(a + b)
    user_prompt = input('Do you wish to repeat (y / n) ?\t')
    if user_prompt == 'n':
        break
