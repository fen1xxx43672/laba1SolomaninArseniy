import time
import random

def second_max(arr):
    if len(arr) < 2:
        return None
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max2

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    random.seed(42)
    print("=== ВТОРОЙ МАКСИМУМ ===")
    print("n\tвремя(с)")
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(second_max, arr)
        print(f"{n}\t{t:.6f}")