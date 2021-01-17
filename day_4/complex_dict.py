"""
key: lists, boolean, dict
"""

complex_dict = {
    'hello': 100,
    100: 'world',
    3.14: 'pi',
    'pi': 3.14,
    'e': 2.71828,
    'hi': print('--hello--'),
    'hey': print,
    10: [1, 10.5, False, [2, 3], range(10), {
        range(2): range(5, 10, 2)
    }],
    67.45: False
}

print(complex_dict[10][5])

complex_dict[10][-1]['hello'] = [1, 2, 3, 4]
complex_dict[10][-1]['hello'].append(45)

for item in complex_dict[10][-1]['hello']: # [1, 2, 3, 4]
    print(item)

# for item in range(5, 10, 2):
#     print(item)

# for key, value in complex_dict.items():
#     print(type(key), type(value))

# a = print
# b = a

# complex_dict['hey']('hello world', end=' *** \n\n')
# print('hello world')
# a('hello world')
# b('hello world')

# var = print(print('hello'))
# print(var)

# f(g(x))



"""
output
var = print(print('hello'))
--- print()
--- print('hello')
-------- print
-------- 'hello' ==> 
-------- return None
--- print(None) ==>> None
var = None
print(var)
print(None) ==> None

hello
None
None
"""
