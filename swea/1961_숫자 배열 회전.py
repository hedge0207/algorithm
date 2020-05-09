import sys
sys.stdin = open("1961_input.txt", "r")

def turn(a):
    tmp = [[""]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-i-1] = a[i][j]
    return tmp

def result(array, col):
    for i in range(N):
        for j in range(N):
            ans[i][col] += array[i][j]
#
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
#
    ans = [[''] * 3 for _ in range(N)]

    for i in range(3):
        arr = turn(arr)
        result(arr,i)

    print("#{}".format(tc))
    for i in range(N):
        for j in range(3):
            print(ans[i][j], end=" ")
        print()



    #풀이2
    # tmp = [[0]*N for _ in range(N)]
    # tmp2 = [[0]*N for _ in range(N)]
    # tmp3 = [[0]*N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         tmp[i][j] = arr[j][N-i-1]
    #
    # for i in range(N):
    #     for j in range(N):
    #         tmp2[i][j] = tmp[j][N-i-1]
    #
    # for i in range(N):
    #     for j in range(N):
    #         tmp3[i][j] = tmp2[j][N-i-1]
    #
    # for i in range(N):
    #     print(''.join(map(str, tmp3[i])), ''.join(map(str, tmp2[i])), ''.join(map(str, tmp[i])))


