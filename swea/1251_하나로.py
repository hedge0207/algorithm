import sys
sys.stdin = open("1251_input.txt", "r")

def f():
    global result
    INF = float('inf')
    key = [INF] * N
    mst = [0] * N

    key[0] = 0
    cnt = 0

    while cnt < N:
        Min = INF
        u = -1

        for i in range(N):
            if not mst[i] and key[i] < Min:
                Min = key[i]
                u = i

        # u를 MST로 선택(새로운 정점으로 선택)
        mst[u] = 1
        result += Min
        cnt += 1

        # key 값을 갱신
        # u에 인접하면서 아직 MST가 아닌 정점 w에서 key[w]>u ↔ w 면(현재 저장된 가중치가 현재 선택된 정점 u와의 사이에서 가중치가 크면) 갱신
        for j in range(N):
            if key[j] > (rl[u] - rl[j]) ** 2 + (cl[u] - cl[j]) ** 2:
                key[j] = (rl[u] - rl[j]) ** 2 + (cl[u] - cl[j]) ** 2


for tc in range(1, int(input()) + 1):
    N = int(input())
    cl = list(map(int,input().split()))
    rl = list(map(int,input().split()))
    E = float(input())
    result = 0

    f()
    print("#{} {}".format(tc,round(result*E)))
