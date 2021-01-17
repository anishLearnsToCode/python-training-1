"""
def function_name(parameter_1, parameter_2, parameter_3 ...):
    code
    code
    [optional] return ans_1, ans_2 ...
"""


"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
def hello() -> None:
    print('hello!')
    # return None


# parameters
"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
def full_name(first_name: str, last_name: str, middle_name=None) -> str:
    if middle_name is None:
        return f'{first_name} {last_name}'

    return f'{first_name} {middle_name} {last_name}'


"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
def sum_numbers(a: int, b: int) -> int:
    return a + b


"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
def multiple(k):
    return k, 10


# print(hello)
# print(type(hello))

# invoke
# arguments
print(full_name('anish', 'sachdeva'))
print(full_name('wolfgang', 'mozart', 'amadeus'))
print(full_name('ada', 'lovelace', 'countess'))

print(full_name(last_name='turing', first_name='alan'))
print(full_name(last_name='bach', middle_name='sebastian', first_name='johanss'))

print(full_name('alan', last_name='turing'))

print('hello', end=' ** ')

# full_name('hello', 'world')
# print(full_name())

# print(hello())
# print(None)

# print(print())
# print(None)

val = multiple(sum_numbers(1, 3))
print(val)

# print(sum_numbers('hello', ' world'))
