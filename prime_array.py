from math import sqrt
import time


def primearr(n):
    start_time = time.time()
    isprime = [True] * (n+1)
    isprime[0] = isprime[1] = False
    m = int(sqrt(n))
    for i in range(2, m+1):
        if isprime[i] == False:
            j = 2*i
            while j <= n:
                isprime[j] = False
                j = j+i
    end_time = time.time()
    print(end_time-start_time)
    return isprime


n = int(input("Enter the Value: "))
isprime = primearr(n)
for i in range(1, n+1):
    if isprime[i]:
        print(i, end=" ")
