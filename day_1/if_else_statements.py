"""
if else statements
if condition_1:
    code
    code
elif [optional] condition_2:
    code
elif [optional] condition_3:
    code
..
..
..
..
else [optional]:
    code
"""

number = int(input())
if number == 0:
    print('puny number')
    print(':(')
elif number == 1:
    print('are you joking!!')
elif number < 100:
    print('mehhh')
elif number < 10:
    # unreachable code
    print('sad number')
else:
    print('default case')

print('outside if else block')
