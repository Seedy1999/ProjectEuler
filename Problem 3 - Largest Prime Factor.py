"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math
import time

target = 600851475143


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True


def find_largest_factor(n):
    low_factor = 2
    while n % low_factor != 0:
        low_factor += 1

    return n // low_factor


# Driver function
t0 = time.perf_counter()

largest_factor = target
while not is_prime(largest_factor):
    largest_factor = find_largest_factor(largest_factor)

t1 = time.perf_counter()

print(largest_factor)

elapsed_time = (t1 - t0) * 1000
print(f"Time required : {elapsed_time} msec")

# .35 msec
