"""
WAP to compute cos(x) for given x. The user should supply x and a positive integer n. We compute the cosine of x
using the taylor series and the computation should use all terms in the series up through the term involving
x^n cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + x^8/8! ...
"""

theta = float(input('theta:\t'))
n = int(input('terms:\t'))
result = 0
x = 1.0
dividend = 1.0
factor = 1.0

for i in range(n):
    result += factor * x / dividend
    factor *= -1
    x *= theta ** 2
    dividend *= (2 * i + 1) * (2 * i + 2)

print(result)
