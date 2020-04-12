import sys
sys.stdin = open("SW7_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    clist = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                cnt += 1
            else:
                if cnt != 0:
                    clist.append(cnt)
                    cnt = 0

    result_a = []
    for i in clist:
        if i not in result_a:
            a = clist.count(i)
            result_a += str(a), i

    result_b = list(map(int, result_a))


    result = []
    for i in range(0,len(result_b)-1,2):
        result.append([result_b[i],result_b[i+1]])

    for i in range(len(result)-1):
        for j in range(len(result)-1-i):
            if result[j][0]*result[j][1] > result[j+1][0]*result[j+1][1]:
                result[j],result[j+1] = result[j+1], result[j]

    for i in range(len(result) - 1):
        if result[i][0] * result[i][1] == result[i + 1][0] * result[i + 1][1]:
            if result[i][0] > result[i + 1][0]:
                result[i], result[i + 1] = result[i + 1], result[i]

    print("#{}".format(tc),end=" ")
    print("{}".format(len(result)),end=" ")
    for i in range(len(result)):
        for j in range(2):
            print(result[i][j],end=" ")
    print()









