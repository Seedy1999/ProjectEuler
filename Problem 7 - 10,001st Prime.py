"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import time
import math


def is_prime(n):
    if n != int(n):
        return False
    if n <= 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    else:
        max_div = math.floor(math.sqrt(n))
        factor = 5
        while factor <= max_div:
            if n % factor == 0:
                return False
            if n % (factor + 2) == 0:
                return False
            factor += 6
    return True


# ====================== Method 1 =====================
t0 = time.perf_counter()
primes = [2, 3, 5, 7]
prime_wanted = 10001

candidate = 9

while len(primes) < prime_wanted:
    if is_prime(candidate):
        primes.append(candidate)
    candidate += 2

result = primes[-1]
t1 = time.perf_counter()

print(result)
print(f"Method 1 elapsed time: {(t1 - t0) * 1000} msec")
# 104743
