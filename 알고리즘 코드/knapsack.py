'''
#tc
#물건 종류, 배낭에 넣을 수 있는 무게
#물건 무개, 물건 가격
3
3 30
25 10
10 9
10 5
3 30
25 15
10 9
10 5
3 30
5 50
10 60
20 140
'''


def f(n, k, curV, curC):  # 물건 개수, 재귀 깊이, 현재 무게 합, 현재 가격 합
    global ans
    if curV > K:
        return
    if n == k:
        if ans < curC:
            ans = curC
    else:
        A[k] = 1
        f(n, k + 1, curV + V[k], curC + C[k])
        A[k] = 0
        f(n, k + 1, curV, curC)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    V = [0] * N  # 각 물건의 무개
    C = [0] * N  # 각 물건의 가치
    A = [0] * N  # 부분집합 포함 여부

    ans = 0
    for i in range(N):
        V[i], C[i] = map(int, input().split())
    f(N, 0, 0, 0)
    print("{} {}".format(tc, ans))
