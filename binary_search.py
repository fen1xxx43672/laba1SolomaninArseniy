import time
import random

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def generate_sorted_array(n):
    arr = generate_array(n)
    arr.sort()
    return arr

def measure_time(func, data, target):
    start = time.perf_counter()
    func(data, target)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    random.seed(42)
    print("=== БИНАРНЫЙ ПОИСК ===")
    print("n\tвремя(с)")
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_sorted_array(n)
        target = arr[n // 2]
        t = measure_time(binary_search, arr, target)
        print(f"{n}\t{t:.6f}")