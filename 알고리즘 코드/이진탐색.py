# 재귀
def binary_search_recursion(st, ed, t):
    if st > ed:
        return

    m = (st + ed) // 2

    if t == arr[m]: #값을 찾았으면 index를 반환
        return m

    elif t < arr[m]:
        return binary_search_recursion(st, m - 1, t)

    else:
        return binary_search_recursion(m + 1, ed, t)


arr = [0,4,8,7,9,2,1,6,3,5]
arr.sort()   #이진 탐색은 정렬이 되어야 사용할 수 있다.
print(arr)
print(binary_search_recursion(0,len(arr)-1,3)) #찾으려는 값인 3의 index를 반환



# 반복
def binary_search_loop(element, some_list):
    st = 0
    ed = len(some_list)-1
    while True:
        mid = (st+ed)//2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            ed = mid-1
        else:
            st = mid+1
        if st > ed:
            return None
print(binary_search_loop(3,arr))  #찾으려는 값인 3의 index를 반환

