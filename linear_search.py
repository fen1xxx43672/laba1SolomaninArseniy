import time
import random

def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data, target):
    start = time.perf_counter()
    func(data, target)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    random.seed(42)
    print("=== ЛИНЕЙНЫЙ ПОИСК ===")
    print("n\tвремя(с)")
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        target = arr[n // 2]
        t = measure_time(linear_search, arr, target)
        print(f"{n}\t{t:.6f}")