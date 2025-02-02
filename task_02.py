from typing import List

def merge_two_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Зливає два відсортовані списки в один відсортований.

    Складність: O(n + m), де n і m — довжини двох списків.

    Args:
        list1 (List[int]): Перший відсортований список.
        list2 (List[int]): Другий відсортований список.

    Returns:
        List[int]: Відсортований об'єднаний список.
    """
    merged = []
    i = j = 0

    # Злиття списків, поки не дійдемо до кінця одного з них
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Додаємо залишки списків (якщо є)
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднує k відсортованих списків у один відсортований список.

    Використовує алгоритм попарного злиття (Merge Sort).

    Складність: O(N log k), де:
        - N — загальна кількість елементів у всіх списках,
        - k — кількість списків.

    Args:
        lists (List[List[int]]): Список відсортованих списків.

    Returns:
        List[int]: Відсортований об'єднаний список.
    """
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []
        
        # Попарне злиття списків
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(list1, list2))

        lists = merged_lists  # Оновлюємо списки після злиття

    return lists[0]  # Єдиний залишений список — це об'єднаний результат

# 🔹 Тестуємо функцію
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
