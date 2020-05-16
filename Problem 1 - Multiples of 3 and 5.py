"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time
end = 10

tic = time.perf_counter()
result = sum([x for x in range(end) if (x % 3 == 0 or x % 5 == 0)])
toc = time.perf_counter()
print(result)
print(f"Time : {toc - tic}")

tic = time.perf_counter()
result = sum(range(0, end, 3)) + sum(range(0, end, 5)) - sum(range(0, end, 15))
toc = time.perf_counter()
print(result)
print(f"Time : {toc - tic}")
