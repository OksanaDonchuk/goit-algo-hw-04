import timeit
import random
from insertion import insertion_sort
from merge import merge_sort
from typing import Dict, List, Tuple

def sorting_algorithms() -> Tuple[Dict[str, List[float]], List[int]]:
    """
    Виконує тестування алгоритмів сортування: вставками, злиттям та Timsort.

    Тестування проводиться на наборах даних різного розміру.
    Вимірюється час виконання для кожного алгоритму.

    Returns:
        Tuple[Dict[str, List[float]], List[int]]: 
            - Словник з назвами алгоритмів та списком їх часу виконання.
            - Список розмірів масивів.
    """
    arr_sizes = [100, 1500, 8000]  # Розміри тестових масивів
    sort_results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}

    for size in arr_sizes:
        array = [random.randint(0, 100000) for _ in range(size)]

        sort_results["Insertion Sort"].append(
            timeit.timeit(lambda: insertion_sort(array.copy()), number=1)
        )
        sort_results["Merge Sort"].append(
            timeit.timeit(lambda: merge_sort(array.copy()), number=1)
        )
        sort_results["Timsort"].append(
            timeit.timeit(lambda: sorted(array.copy()), number=1)
        )

    return sort_results, arr_sizes

# Запуск тестів
results, sizes = sorting_algorithms()

# Вивід у вигляді таблиці
print(f"\n{'Size':>10} | {'Insertion Sort':>15} | {'Merge Sort':>10} | {'Timsort':>10}")
print("-" * 50)

for i, size in enumerate(sizes):
    print(
        f"{size:>10} | {results['Insertion Sort'][i]:>15.5f} | "
        f"{results['Merge Sort'][i]:>10.5f} | {results['Timsort'][i]:>10.5f}"
    )
