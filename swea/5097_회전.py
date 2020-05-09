import sys
sys.stdin = open('5097_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    que=[1,2,3]



    a = 0
    for i in range(M+1):
        if a==N:
            a=0
        if len(que)==N:
            que.pop(0)
            que.append(arr[a])
        else:
            que.append(arr[a])
        a+=1

    print("#{} {}".format(tc,que[-1]))





