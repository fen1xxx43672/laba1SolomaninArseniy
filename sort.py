import time
import random
import sys


class Element:
    def __init__(self, value):
        self.value = value


def insertion_sort(unsorted, n):
    " сортировка вставками "
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        val = unsorted[i].value
        hole = i
        comparisons += 1

        while hole > 0 and unsorted[hole - 1].value > val:
            unsorted[hole].value = unsorted[hole - 1].value
            hole -= 1
            swaps += 1
            if hole > 0:
                comparisons += 1

        unsorted[hole].value = val

    return comparisons, swaps


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(Element(random.randint(0, 10000)))
    return arr


def measure_time_and_ops(arr):
    start = time.perf_counter()
    comparisons, swaps = insertion_sort(arr, len(arr))
    end = time.perf_counter()
    return end - start, comparisons, swaps


def measure_memory(arr):
    " измерение пространственной сложности "
    arr_copy = arr.copy()
    before = sys.getsizeof(arr_copy)
    for elem in arr_copy:
        before += sys.getsizeof(elem)

    insertion_sort(arr_copy, len(arr_copy))

    after = sys.getsizeof(arr_copy)
    for elem in arr_copy:
        after += sys.getsizeof(elem)

    return after - before


def measure_memory_during_sort(arr):
    """ измерение памяти во время сортировки """
    import tracemalloc

    arr_copy = arr.copy()
    tracemalloc.start()

    insertion_sort(arr_copy, len(arr_copy))

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak / 1024 / 1024


if __name__ == '__main__':
    random.seed(42)

    print("=== СОРТИРОВКА ВСТАВКАМИ ===")
    print("Анализ алгоритмической и пространственной сложности")
    print()
    print(f"{'n':>8} {'время(с)':>12} {'сравнения':>12} {'обмены':>12} {'память(МБ)':>12}")
    print("-" * 60)

    sizes = [100, 500, 1000, 2000, 5000, 10000]

    for n in sizes:
        arr = generate_array(n)

        t, comp, swaps = measure_time_and_ops(arr)
        mem = measure_memory_during_sort(arr)

        print(f"{n:8} {t:12.6f} {comp:12} {swaps:12} {mem:12.6f}")

    print("\n")
    print("=== ТЕОРЕТИЧЕСКАЯ СЛОЖНОСТЬ ===")
    print("Временная сложность: O(n²)")
    print("Пространственная сложность: O(1)")