def heapify(arr, n, i):
    largest = i  # Инициализируем корень как самый большой элемент
    left = 2 * i + 1  # левый дочерний элемент
    right = 2 * i + 2  # правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами

        # Рекурсивно преобразуем затронутое поддерево в кучу
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # перемещаем текущий корень в конец
        heapify(arr, i, 0)  # вызываем heapify на уменьшенной куче

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:", arr)