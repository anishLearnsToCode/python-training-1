"""
Time Complexity: O(1)
Space Complexity: O(1)
"""

"""
While Loop

while condition:
    code
    code

condition (if true) --> code --> condition (if true) --> code --> condition (if true) --> code --> condition (false) --> exit
"""

# infinite loop
# while True:
#     print('hello')

# dry run

i = 5

while i <= 10:
    print(i)
    i = i * 2


print(i)
print('i am outside loop')

"""
i = 20
5
10
20
i am outside loop
"""