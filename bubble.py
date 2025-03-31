def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем местами, если элемент найден больше, чем следующий
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Пример использования
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", arr)
    bubble_sort(arr)
    print("Отсортированный массив:", arr)