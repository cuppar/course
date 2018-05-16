import math


def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    isPrime = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime


for i in range(10):
    print('prime(', i, ') : ', prime(i), sep='')
