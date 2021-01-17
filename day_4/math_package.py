# bad bad bad ohh so very bad practice
# from math import *

"""
Time Complexity: O(number)
Space Complexity: O(1)
"""

# alias
import math
import time
import day_4.number_theory as nt

number = 6700417
start_1 = time.time()
print('Prime' if nt.is_prime(number) else 'Not Prime')
start_2 = time.time()
print('Prime' if nt.is_prime_linear(number) else 'Not Prime')
start_3 = time.time()

print(f'Time taken by fast {start_2 - start_1}')
print(f'Time taken by slow {start_3 - start_2}')
