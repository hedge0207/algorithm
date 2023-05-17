def merge(arr1, arr2):
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)
    sorted_arr = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    if i == n:
        sorted_arr += arr2[j:]

    if j == m:
        sorted_arr += arr1[i:]

    return sorted_arr


def merge_sort(arr):
    if (length := len(arr)) < 2:
        return arr

    lh = arr[:length // 2]
    rh = arr[length // 2:]
    return merge(merge_sort(lh), merge_sort(rh))


arr = [2, 5, 7, 3, 8, 9, 4, 1]
print(merge_sort(arr))
