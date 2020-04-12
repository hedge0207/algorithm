def merge(list1, list2):
    i = 0
    j = 0

    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    if i == len(list1):
        result+=list2[j:]  #이 부분을 append로 쓸 경우 오류가 발생
    else:
        result+=list1[i:]  #이 부분을 append로 쓸 경우 오류가 발생

    return result


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    lh = my_list[:len(my_list) // 2]
    rh = my_list[len(my_list) // 2:]

    return merge(merge_sort(lh), merge_sort(rh))


print(merge_sort([13,7,1]))


