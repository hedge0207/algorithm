#ver1. 정답은 맞음
# N, M = map(int, input().split())
# a = []
# u = [0] * (N + 1)
#
#
# def backtrack(k,c):
#     if k == M:
#         for i in range(M):
#             print(a[i], end=" ")
#         print()
#     else:
#         for i in range(1, N + 1):
#             if i>c:
#                 c+=1
#                 if u[i]:
#                     continue
#                 else:
#                     u[i] = 1
#                     a.append(i)
#                     backtrack(k+1,c)
#                     a.pop()
#                     u[i] = 0
#
# backtrack(0,0)


#ver2. 표준 방식
N, M = map(int, input().split())
a = []
u = [0] * (N + 1)


def backtrack(k,c):
    if k == M:
        for i in range(M):
            print(a[i], end=" ")
        print()
    else:
        for i in range(c, N + 1):
            if u[i]:
                continue
            else:
                u[i] = 1
                a.append(i)
                backtrack(k+1,i)
                a.pop()
                u[i] = 0

backtrack(0,1)