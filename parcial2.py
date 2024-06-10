from numpy import sqrt
from math import gcd


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, sqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def areCoprimes(a, b):
    return gcd(a, b) == 1


def countCoprimes(n):
    count = 0
    for i in range(1, n):
        if areCoprimes(n, i):
            count += 1
    return count

print(countCoprimes(323))
