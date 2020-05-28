import sys

sys.stdin = open("1244_input.txt", "r")

# def f(k, c, r):
#     global Max
#     if k == c:
#         tmp = ''
#         for i in r:
#             tmp += i
#         if int(tmp) > Max:
#             Max = int(tmp)
#         return
#
#     for i in range(len(r) - 1):
#         for j in range(i + 1, len(r)):
#             r[i], r[j] = r[j], r[i]
#
#             tmp2 = ''
#             for q in r:
#                 tmp2 += q
#
#             # 현재 깊이에 이미 동일한 값이 있었으면 동일한 재귀를 무의미하게 반복하는 것이므로 continue
#             if tmp2 in check[k]:
#                 r[i], r[j] = r[j], r[i]  #배열을 다시 돌려준다.
#                 continue
#
#             check[k].append(tmp2)
#             f(k + 1, c, r)
#             r[i], r[j] = r[j], r[i]
#
#
# for tc in range(1, int(input()) + 1):
#     tmp1, tmp2 = input().split()
#     Max = -1
#     n = list(tmp1)
#     c = int(tmp2)
#     check = [[] for _ in range(c)]  #깊이 별로 값들의 중복을 체크하기 위한 배열
#     f(0, c, n)
#
#     print("#{} {}".format(tc,Max))


# 교수님 풀이1-BFS
# from collections import deque
#
# d = [1, 10, 100, 1000, 10000, 100000]
#
# for tc in range(1, int(input()) + 1):
#     arr, N = input().split()
#     L = len(arr)
#     N = int(N)
#
#     ans = 0
#     visit = [set() for _ in range(N + 1)]
#
#     Q = deque()
#     Q.append((int(arr), 0))
#     while Q:
#         val, k = Q.popleft()
#
#         if k == N:
#             ans = max(ans, val)
#         else:
#             for i in range(L - 1):
#                 for j in range(i + 1, L):
#                     a = (val // d[i]) % 10
#                     b = (val // d[j]) % 10
#                     t = val - a * d[i] + b * d[i] - b * d[j] + a * d[j]
#                     if t in visit[k + 1]:
#                         continue
#                     visit[k + 1].add(t)
#                     Q.append((t, k + 1))
#     print(ans)




#교수님 풀이2-DFS
d = [1, 10, 100, 1000, 10000, 100000]

visit = [[0]*1000000 for _ in range(11)] #visit을 매 테스트 케이스마다 생성하지 않고
for tc in range(1, int(input()) + 1):
    num, cnt = input().split()
    N = len(num)
    num = list(map(int,num))
    cnt = int(cnt)

    ans = 0

    def getVal():
        ret = 0
        for v in num:
            ret = ret*10+v
        return ret

    def backtrack(k):
        val = getVal()
        if visit[k][val]==tc:  #tc를 활용한다.
            return
        visit[k][val] = tc

        if k==cnt:
            global ans
            ans = max(ans,getVal())
        else:
            for i in range(N - 1):
                for j in range(i + 1, N):
                    num[i],num[j]=num[j],num[i]
                    backtrack(k+1)
                    num[i], num[j] = num[j], num[i]

    backtrack(0)
    print(ans)