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
    if j==len(list2):  #else로 쓸 경우 특정 배열에서는 에러가 발생 반드시 if로 써야 한다.
        result+=list1[i:]  #이 부분을 append로 쓸 경우 오류가 발생
    return result


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    lh = my_list[:len(my_list) // 2]
    rh = my_list[len(my_list) // 2:]

    return merge(merge_sort(lh), merge_sort(rh))


print(merge_sort([13,7,1,12,8,4,2,8,7]))