import sys
sys.stdin = open("1248_input.txt", "r")


def f(node, flag, arr):  #공통 조상을 찾기 위한 함수
    global com, tmp
    if node in arr:
        com = node
        return
    if flag:
        arr.append(node)
    if parent[node] == 0:
        tmp = arr[:]
        return
    f(parent[node], flag, arr)


def search(node):
    global cnt
    if node == 0:
        return

    search(left[node])
    cnt += 1
    search(right[node])


for tc in range(1, int(input()) + 1):
    V, E, N1, N2 = map(int, input().split())
    edges = list(map(int, input().split()))
    parent = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for i in range(0, len(edges), 2):
        p, c = edges[i], edges[i + 1]
        if left[p]:
            right[p] = c
        else:
            left[p] = c
        parent[c] = p

    com = 0  #공통 조상을 저장할 변수
    tmp = []  #N1에서 루트까지 가는 경로를 저장할 배열
    f(N1, 1, [])
    f(N2, 0, tmp)

    cnt = 0
    search(com)

    print("#{} {} {}".format(tc, com, cnt))