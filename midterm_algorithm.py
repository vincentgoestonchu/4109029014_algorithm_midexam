import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False

def fibonacci_search(arr, x):
    fib2 = 0
    fib1 = 1
    fib0 = fib2 + fib1
    offset = -1

    while fib0 < len(arr):
        fib2 = fib1
        fib1 = fib0
        fib0 = fib2 + fib1

    while fib0 > 1:
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < x:
            fib0 = fib1
            fib1 = fib2
            fib2 = fib0 - fib1
            offset = i
        elif arr[i] > x:
            fib0 = fib2
            fib1 = fib1 - fib2
            fib2 = fib0 - fib1
        else:
            return i

    if fib1 == 1 and offset < len(arr) - 1 and arr[offset + 1] == x:
        return offset + 1
    else:
        return -1

random.seed(42)
results = []
for n in range(10, 101, 10):
    S = [random.randint(1, 1000) for _ in range(n)]
    x = random.randint(1, 1000)
    print(f"List size: {n}")
    total_linear_search_time = 0
    total_binary_search_time = 0
    total_fibonacci_search_time = 0

    for _ in range(5):
        start_time = time.perf_counter()
        linear_search(S, x)
        end_time = time.perf_counter()
        total_linear_search_time += end_time - start_time

        start_time = time.perf_counter()
        binary_search(S, x)
        end_time = time.perf_counter()
        total_binary_search_time += end_time - start_time

        start_time = time.perf_counter()
        fibonacci_search(S, x)
        end_time = time.perf_counter()
        total_fibonacci_search_time += end_time - start_time

    avg_linear_search_time = total_linear_search_time / 5
    avg_binary_search_time = total_binary_search_time / 5
    avg_fibonacci_search_time = total_fibonacci_search_time / 5
    print(f"Avg. Linear Search Time: {avg_linear_search_time:.6f} seconds")
    print(f"Avg. Binary Search Time: {avg_binary_search_time:.6f} seconds")
    print(f"Avg. Fibonacci Search Time: {avg_fibonacci_search_time:.6f} seconds")
    print("------")

total_avg_linear_search_time = sum(avg_linear_search_time for n in range(10, 101, 10)) / 10
total_avg_binary_search_time = sum(avg_binary_search_time for n in range(10, 101, 10)) / 10
total_avg_fibonacci_search_time = sum(avg_fibonacci_search_time for n in range(10, 101, 10)) / 10
print("Overall Average Search Time:")
print(f"Avg. Linear Search Time: {total_avg_linear_search_time:.6f} seconds")
print(f"Avg. Binary Search Time: {total_avg_binary_search_time:.6f} seconds")
print(f"Avg. Fibonacci Search Time: {total_avg_fibonacci_search_time:.6f} seconds")