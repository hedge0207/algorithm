import sys
sys.stdin = open("1486_input.txt", "r")

# def f(k,sl):
#     global Min
#     if k==N:
#         if sl>=B and Min>sl:
#             Min=sl
#         return
#     f(k+1,sl+length[k])
#     f(k+1,sl)
#
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N,B = map(int,input().split())
#     length = list(map(int, input().split()))
#     Min = 0xffffff
#     f(0,0)
#     print("#{} {}".format(tc,Min-B))


#약간 개선
def f(k,s):
    global Min
    if s>Min:
        return
    if k==N:
        if s>=B and s<Min:
            Min=s
        return
    subset.append(heigth[k])
    f(k+1,s+heigth[k])
    subset.pop()
    f(k+1,s)

T = int(input())

for tc in range(1,T+1):
    N,B = map(int,input().split())
    heigth = list(map(int,input().split()))
    Min=200000
    subset = []
    f(0,0)
    print("#{} {}".format(tc,Min-B))


# 반복문 풀이
# T = int(input())
# for tc in range(1,T+1):
#     N,B = map(int,input().split())
#     length = list(map(int, input().split()))
#
#     slist = []
#     for i in range(1<<N):
#         a = 0
#         for j in range(N+1):
#             if i & (1<<j):
#                 a += length[j]
#             if a >= B:
#                 slist.append(a)
#
#     result = []
#     for i in range(len(slist)):
#         if slist[i] > B:
#             result.append(slist[i])
#
#     print("#{} {}".format(tc, min(slist) - B))


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




