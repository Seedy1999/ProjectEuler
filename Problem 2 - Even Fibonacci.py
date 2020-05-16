"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
import time
tic = time.perf_counter()
max_val = 4000000
prev, val = 1, 2
result = 0
while val <= max_val:
    if val % 2 == 0:
        result += val

    prev, val = val, prev + val
toc = time.perf_counter()
print(result)
print(f"Elapsed Time: {toc - tic}")
