import sys

sys.stdin = open('9317_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = input()
    S = input()

    cnt = 0
    for i in range(N):
        if A[i] == S[i]:
            cnt += 1

    print("#{} {}".format(tc, cnt))
