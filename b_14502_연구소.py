import sys
sys.setrecursionlimit(1000000)

#시간초과로 인해 pypy로 제출, 아래에 수정 후 파이썬으로 통과한 코드 있음
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bw(k,c):
    if k == 3:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    vi(i, j)
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
                if arr[i][j] == 3:
                    arr[i][j] = 0
        cntl.append(cnt)

    else:
        for i in range(N):
            if i<c:
                continue
            for j in range(M):
                if arr[i][j] > 0:
                    continue
                arr[i][j] = 1
                bw(k + 1,i)
                arr[i][j] = 0


def vi(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if arr[nr][nc] == 0:
            arr[nr][nc] = 3
            vi(nr, nc)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cntl = []

bw(0,0)
print(max(cntl))






#수정해서 파이썬으로 통과한 코드
# import sys
# sys.setrecursionlimit(1000000)
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def bw(k,c):
#     if k == 3:
#         for i in range(N):
#             for j in range(M):
#                 if arr[i][j] == 2:
#                     vi(i, j)
#         cnt = 0
#         for i in range(N):
#             for j in range(M):
#                 if arr[i][j] == 0:
#                     cnt += 1
#                 if arr[i][j] == 3:
#                     arr[i][j] = 0
#         cntl.append(cnt)
#
#     else:
#         for i in range(c,N):    #이 부분을 추가
#             for j in range(M):
#                 if arr[i][j] > 0:
#                     continue
#                 arr[i][j] = 1
#                 bw(k + 1,i)
#                 arr[i][j] = 0
#
#
# def vi(r, c):
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr < 0 or nr >= N or nc < 0 or nc >= M:
#             continue
#         if arr[nr][nc] == 0:
#             arr[nr][nc] = 3
#             vi(nr, nc)
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cntl = []

bw(0,0)
print(max(cntl))