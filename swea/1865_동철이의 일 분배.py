import sys
sys.stdin = open('1865_input.txt', 'r')


# def assign(c,proba):
#     global Max
#     if c==N:
#         if Max<proba:
#             Max=proba
#     #소수의 곱이기 때문에 다음 확률을 곱해도 더 높아질 수는 없다.
#     #확률이 100%인 경우라도 결국 1을 곱하는 것이기 때문에 확률에는 변화가 없다.
#     #따라서 중간까지 구한 확률이 최대확률보다 낮다면 return시킨다.
#     elif Max >= proba:
#         return
#     else:
#         for i in range(N):
#             if aw[i]==0:
#                 aw[i]=1
#                 assign(c+1,proba*task[i][c]/100)
#                 aw[i]=0
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     task = [list(map(int,input().split())) for _ in range(N)]
#     Max=0
#     aw = [0]*N
#     assign(0,1)
#     Max*=100
#     print("#{} {:.6f}".format(tc,Max))


# 200907 재풀이
def assign(k, p):
    global Max
    if k == N:
        if p > Max:
            Max = p
        return
    if Max>=p:
        return
    for i in range(N):
        if not assignment[i]:
            assignment[i]=1
            assign(k+1, p * task[i][k] / 100)
            assignment[i]=0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    assignment = [0]*N
    assign(0, 1)
    print("#{} {:.6f}".format(tc, Max*100))
