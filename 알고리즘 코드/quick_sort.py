# 로무토 방식
def lomuto_partition(arr, low, high):
    # pivot으로 배열의 가장 오른쪽 값을 선택
    pivot = arr[high]
    left = low
    for right in range(low, high):
        if arr[right] < pivot:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1

    arr[left], arr[high] = arr[high], arr[left]

    # pivot을 반환한다.
    return left


def lomuto_quick_sort(arr, low, high):
    # 재귀적으로 호출되더라도 원본 배열 arr의 크기는 변하지 않는다.
    # 따라서 아래와 같이 base condition을 설정해준다.
    if low < high:
        pivot = lomuto_partition(arr, low, high)
        # pivot 기준 왼쪽 정렬
        lomuto_quick_sort(arr, low, pivot - 1)
        # pivot 기준 오른쪽 정렬
        lomuto_quick_sort(arr, pivot + 1, high)


lst = [2, 4, 5, 2, 1, 4, 6, 7, 2, 9]
lomuto_quick_sort(lst, 0, len(lst) - 1)


# 호어 방식
def hoare_partition(arr, left, right):
    i = left
    j = right
    pivot = arr[left]
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def hoare_quick_sort(arr, low, high):
    if low < high:
        pivot = hoare_partition(arr, low, high)
        hoare_quick_sort(arr, low, pivot - 1)
        hoare_quick_sort(arr, pivot + 1, high)


lst = [2, 4, 5, 2, 1, 4, 6, 7, 2, 9]
hoare_quick_sort(lst, 0, len(lst) - 1)
print(lst)
