import time
import random

def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    print("=== ТАБЛИЦА УМНОЖЕНИЯ ===")
    print("n\tвремя(с)\tэлементов")
    table_sizes = [100, 200, 500, 1000]
    for n in table_sizes:
        t = measure_time(multiplication_table, n)
        print(f"{n}\t{t:.6f}\t{n*n}")