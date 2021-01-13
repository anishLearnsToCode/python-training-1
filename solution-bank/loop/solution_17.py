"""
WAP to compute sin(x) for given x. The user should supply x and a positive integer n. We compute the sine of x using
the taylor series and the computation should use all terms in the series up through the term involving
x^n sin(x) = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! ...
3! = 1 * 2 * 3 * (4 * 5) = 5! * (6 * 7) = 7!
"""

theta = float(input('theta:\t'))
n = int(input('terms:\t'))
result = 0
x = theta
divisor = 1.0
factor = 1.0

for i in range(n):
    result += factor * x / divisor
    factor *= -1
    x *= theta ** 2
    divisor *= (2 * i + 2) * (2 * i + 3)

print(result)
