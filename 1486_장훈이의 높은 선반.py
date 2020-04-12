import sys
sys.stdin = open("1486_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    length = list(map(int, input().split()))

    slist = []
    for i in range(1<<N):
        a = 0
        for j in range(N+1):
            if i & (1<<j):
                a += length[j]
            if a >= B:
                slist.append(a)

    result = []
    for i in range(len(slist)):
        if slist[i] > B:
            result.append(slist[i])

    print("#{} {}".format(tc, min(slist) - B))


    # 처음엔 아래와 같이 했으나 시간초과 발생
    # slist = []
    # MIN = 987654321
    # for i in range(1<<N):
    #     a = 0
    #     for j in range(N+1):
    #         if i & (1<<j):
    #             a += length[j]
    #             if B < a:
    #                 MIN = a
    #             if MIN < a:
    #                 MIN = 987654321
    #                 continue
    #         if a not in slist and B < a:
    #             slist.append(a)
    #
    # print("#{} {}".format(tc,min(slist)-B))




