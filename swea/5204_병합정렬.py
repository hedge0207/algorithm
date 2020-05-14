import sys
sys.stdin=open("5204_input.txt",'r')

def merge(list1, list2):
    global cnt
    i = 0
    j = 0
    le = list1[-1]
    re = list2[-1]
    if le>re:
        cnt+=1

    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    if i == len(list1):
        result+=list2[j:]
    if j == len(list2):
        result+=list1[i:]
    return result


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list

    lh = my_list[:len(my_list) // 2]
    rh = my_list[len(my_list) // 2:]

    return merge(merge_sort(lh), merge_sort(rh))

for tc in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt=0
    sarr=merge_sort(arr)
    print("#{} {} {}".format(tc,sarr[N//2],cnt))
