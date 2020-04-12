import sys
sys.stdin = open("1284_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())

    A = W*P
    if W <= R:
        B = Q
    else:
        B = Q+((W-R)*S)

    if A > B:
        print("#{} {}".format(tc,B))
    else:
        print("#{} {}".format(tc, A))