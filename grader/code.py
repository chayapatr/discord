from math import floor

x = int(input())

# LARGE PRIMES
# 2147483647
# 999999000001
# 67280421310721

def prime_check(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, floor(x ** (1/2)) + 1):
        # print("{x} % {i} = {res}".format(x=x, i=i, res=x%i))
        if x % i == 0:
            return False
    
    return True

k = prime_check(x)
if k:
    print("YES")
else:
    print("NO")