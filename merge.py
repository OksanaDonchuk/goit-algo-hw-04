from typing import List

def merge_sort(arr: List[int]) -> None:
    """
    Реалізує сортування злиттям (Merge Sort).

    Алгоритм використовує принцип "розділяй і володарюй":
    - Ділить масив на дві частини, рекурсивно сортує кожну,
    - Потім об'єднує їх у відсортований масив.

    Складність:
    - Найгірший, найкращий і середній випадки: O(n log n)

    Args:
        arr (List[int]): Масив, який потрібно відсортувати.

    Returns:
        None: Сортування відбувається на місці.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Злиття двох частин
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Додаємо залишки з L, якщо такі є
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Додаємо залишки з R, якщо такі є
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
