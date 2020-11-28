import math
val = math.factorial(5)
def fact(n):
    val = 1
    for i in range(2,n + 1):
            val *= i
    return val
for i in range(1,10):
    print('fact({})={}'.format(i,fact(i)))

