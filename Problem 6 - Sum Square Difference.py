"""
The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import time
start = 1
end = 100

# ================ Method 1 =====================
t0 = time.perf_counter()
result = (sum(range(start, end + 1)))**2 - sum([x**2 for x in range(start, end + 1)])
t1 = time.perf_counter()
print(result)
print(f"Method 1 elapsed time: {(t1 - t0) * 1000} msec")

# ================= Method 2 =======================
t0 = time.perf_counter()
sum_squared = ((end * (end + 1)) // 2) ** 2
sum_of_squares = sum([x**2 for x in range(start, end + 1)])
result = sum_squared - sum_of_squares
t1 = time.perf_counter()
print(result)
print(f"Method 2 elapsed time: {(t1 - t0) * 1000} msec")

# ================= Method 2 =======================
t0 = time.perf_counter()
sum_squared = ((end * (end + 1)) // 2) ** 2
sum_of_squares = ((2 * end + 1) * (end + 1) * end) // 6
result = sum_squared - sum_of_squares
t1 = time.perf_counter()
print(result)
print(f"Method 3 elapsed time: {(t1 - t0) * 1000} msec")