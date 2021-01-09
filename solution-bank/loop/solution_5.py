# WAP to compute a ^ b without using the inbuilt power operator (assume a is integer and b positive integer)

a = float(input('base:\t'))
b = int(input('power:\t'))

result = 1

for i in range(b):
    result *= a

print(result)
