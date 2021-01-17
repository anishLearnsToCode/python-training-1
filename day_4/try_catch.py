import sys, traceback

try:
    n = int(input('enter number:\t'))
    l = [1, 2, 3]
    index = int(input('enter index:\t'))
    print(l[index])
    words = {}
    print(words['hello'])
except Exception as e:
    print('default')
    # print(traceback.format_exc())
    print(e)
except ValueError as e:
    print('i caught value error')
    print(e)
except IndexError as e:
    print('i caught index error')
    print(e)

print('code executed normally')
