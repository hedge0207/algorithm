import sys
sys.stdin = open("5521_input.txt", "r")

for tc in range(1, int(input()) + 1):
    N,M = map(int,input().split())
    friends = [[] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)

    invited = [0] * (N + 1)
    Q = []
    invited[1] = 1
    Q.append(1)
    while Q:
        NQ = []
        for i in Q:
            for j in friends[i]:
                if not invited[j]:
                    invited[j]=invited[i]+1
                    NQ.append(j)
        Q = NQ


    cnt = 0
    for i in invited:
        if i and i<4:
            cnt+=1

    print("#{} {}".format(tc, cnt-1))








# for tc in range(1, int(input()) + 1):
#     N,M = map(int,input().split())
#     friends = [[] for _ in range(N+1)]
#     invite = [0]*(N+1)
#     invite[1]=1
#     for i in range(M):
#         a,b = map(int,input().split())
#         friends[a].append(b)
#         friends[b].append(a)
#
#     cnt = 0
#     for i in friends[1]:
#         if not invite[i]:
#             invite[i] = 1
#             cnt += 1
#         for j in friends[i]:
#             if not invite[j]:
#                 invite[j]=1
#                 cnt+=1
#
#     print("#{} {}".format(tc,cnt))
