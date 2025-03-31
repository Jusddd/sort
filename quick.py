def quick_sort(arr):
    if len(arr) <= 1:  # Базовый случай: массив из 0 или 1 элемента уже отсортирован
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Выбор опорного элемента (средний элемент)
        left = [x for x in arr if x < pivot]  # Элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы равные опорному
        right = [x for x in arr if x > pivot]  # Элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)  # Рекурсивная сортировка

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)