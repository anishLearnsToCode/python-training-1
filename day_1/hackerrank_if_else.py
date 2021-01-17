"""
Time Complexity: O(1)
Space Complexity: O(1)
"""

number = int(input())

if number % 2 == 1 or 6 <= number <= 20:
    print('Weird')
elif 2 <= number <= 5 or number > 20:
    print('Not Weird')


"""
number = 1
1 % 2 == 1 ? True
print('Weird')


number = 101
101 % 2 == 1 ? True
Weird


number = 4
4 % 2 == 1 ? False
6 <= 4 <= 20 ? False
2 <= 4 <= 5 ? True
not weird
"""
