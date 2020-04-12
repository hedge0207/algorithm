import sys
sys.stdin = open("6485_input.txt","r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    bus= [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bs = [int(input()) for _ in range(P)]
    bsc = [0]*5001

    for i in range(len(bus)):
        for j in range(bus[i][0],bus[i][1]+1):
            bsc[j] += 1

    print("#{}".format(tc),end=" ")
    result = ""
    for i in range(P):
        result += str(bsc[bs[i]])+" "
    print(result.rstrip())


    #아래와 같이 출력할 경우 맨 마지막에 공백이 한 칸 생겨 오답이라고 뜬다.
    # for i in range(P):
    #     print(bsc[bs[i]],end=" ")




# 첫 오답
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     bus = [list(map(int, input().split())) for _ in range(N)]
#     P = int(input())
#     bs = [int(input()) for _ in range(P)]
#     bsc = [0] * (P + 1)
#
#     for i in range(N):
#         for j in range(bus[i][0], bus[i][1] + 1):
#             bsc[j] += 1
#
#     print("#{}".format(tc), end=" ")
#     for i in range(1, len(bsc)):
#         print("{}".format(bsc[i]), end=" ")
