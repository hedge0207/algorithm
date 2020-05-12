# def f(k,c):
#     if k==M:
#         for i in l:
#             print(i,end=" ")
#         print()
#     else:
#         for i in range(len(arr)):
#             if visited[i] ==0 and arr[i] not in vl[k]:
#                 vl[k].append(arr[i])
#                 visited[i]=1
#                 l.append(arr[i])
#                 f(k+1,i)
#                 visited[i]=0
#                 l.pop()
#                 if k != M-1:
#                     vl[k+1]=[]
#
#
# N, M = map(int,input().split())
# arr = list(map(int,input().split()))
# visited = [0]*N
# vl = [[] for _ in range(M)]
# arr.sort()
#
# t = []
# l=[]
# f(0,"C")



# 더 나은 풀이
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [0] * N
arr = []

def solve(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return
    a = 0
    for i in range(N):
        if not visited[i] and a != L[i]:
            visited[i] = True
            arr.append(L[i])
            a = L[i]
            solve(k+1)
            visited[i] = False
            arr.pop()

solve(0)