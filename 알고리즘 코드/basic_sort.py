def selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        index_min = i
        for j in range(i + 1, length):
            if arr[index_min] > arr[j]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]


def bubble_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]