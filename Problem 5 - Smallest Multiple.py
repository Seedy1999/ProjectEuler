"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

# ==================== Method 1 ========================================
t0 = time.perf_counter()

candidate = 0
divisors = range(11, 20)

finished = False
while not finished:
    candidate += 20
    finished = True
    for div in divisors:
        if candidate % div != 0:
            finished = False
            break

print(candidate)
