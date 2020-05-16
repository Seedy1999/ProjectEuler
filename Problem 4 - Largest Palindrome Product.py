"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

# =================== Method 1 =============================
t0 = time.perf_counter()

palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            palindromes.append(product)

t1 = time.perf_counter()
print(max(palindromes))

print(f"Method 1 Elapsed time: {(t1 - t0) * 1000} msec")


# =================== Method 2 =============================
t0 = time.perf_counter()

largest_palindrome = 0
a = 999
while a >= 100:
    b = 999
    while b >= a:
        this_product = a * b
        if a * b <= largest_palindrome:
            break
        if str(this_product) == str(this_product)[::-1]:
            largest_palindrome = this_product
        b = b - 1
    a = a - 1

t1 = time.perf_counter()

print(largest_palindrome)
print(f"Method 2 Elapsed time: {(t1 - t0) * 1000} msec")
