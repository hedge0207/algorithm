def partion(my_list, st, ed):
    a = st
    b = st
    p = ed

    while a < p:
        if my_list[a] <= my_list[p]:
            my_list[a], my_list[b] = my_list[b], my_list[a]
            b += 1
        a += 1
    #위 과정이 끝나면 b를 기준으로 p보다 큰 값과 작은 값이 나뉘게 되고 b가 가리키는 값(my_list[b]) 또한 p가 가리키는 값보다 항상 크다.
    #본래 p를 기준으로 좌측에는 p보다 작은 값, 우측에는 p보다 큰 값을 오게 하려는 함수이므로 아래와 같은 과정을 통해 p와 b를 바꿔준다.
    print(p,b,my_list)
    my_list[b], my_list[p] = my_list[p], my_list[b]
    p = b
    print(my_list)
    return p


def quick(my_list, st, ed):
    if ed - st < 1:    #재귀적으로 호출되면서 파라미터 start와 end만 바뀔 뿐, my_list는 바뀌지 않는다. 따라서 다른 방법으로 정렬하려는 리스트의 길이가 1이라는 것을 표현해야 한다.
        return
    p = partion(my_list, st, ed)
    # p 기준으로 왼쪽을 정렬
    quick(my_list, st, p - 1)
    # p 기준으로 오른쪽을 정렬
    quick(my_list, p + 1, ed)


a = [5, 4, 3, 7, 5, 15, 3, 2, 1]
quick(a, 0, len(a) - 1)
print(a)
