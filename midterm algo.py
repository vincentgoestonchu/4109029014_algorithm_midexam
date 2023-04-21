import random
import time
import matplotlib.pyplot as plt

def linear_search(S, x):
    for num in S:
        if num == x:
            return True
    return False

def binary_search(S, x):
    low = 0
    high = len(S) - 1

    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False

def fibonacci_search(S, x):
    n = len(S)
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    while fib_m < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib_m > 1 and (offset + fib_m_minus_2) < n:
        i = min(offset + fib_m_minus_2, n - 1)

        if S[i] < x:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i
        elif S[i] > x:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
        else:
            return i

    if fib_m_minus_1 and (offset + 1) < n and S[offset + 1] == x:
        return offset + 1

    return -1

# Generate list S and integer x
n_values = list(range(100, 10001, 100))
linear_search_times = []
binary_search_times = []
fibonacci_search_times = []

for n in n_values:
    S = random.sample(range(1, n + 1), n)
    x = random.randint(1, n)

    # Perform 5 iterations and calculate average execution time
    linear_search_total_time = 0
    binary_search_total_time = 0
    fibonacci_search_total_time = 0

    for _ in range(5):
        start_time = time.time()
        linear_search(S, x)
        end_time = time.time()
        linear_search_total_time += end_time - start_time

        start_time = time.time()
        binary_search(S, x)
        end_time = time.time()
        binary_search_total_time += end_time - start_time

        start_time = time.time()
        fibonacci_search(S, x)
        end_time = time.time()
        fibonacci_search_total_time += end_time - start_time

    linear_search_avg_time = linear_search_total_time / 5
    binary_search_avg_time = binary_search_total_time / 5
    fibonacci_search_avg_time = fibonacci_search_total_time / 5

    linear_search_times.append(linear_search_avg_time)
    binary_search_times.append(binary_search_avg_time)
    fibonacci_search_times.append(fibonacci_search_avg_time)

# Plot the line chart
plt.plot(n_values, linear_search_times, label='Linear Search')
plt.plot(n_values, binary_search_times, label='Binary Search')
plt.plot(n_values, fibonacci_search_times, label='Fibonacci Search')
plt.xlabel('n')
plt.ylabel('Average Execution Time (s)')
plt.legend()
plt.show()