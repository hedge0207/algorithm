import sys
sys.stdin=open("5208_input.txt",'r')

def f(k,d,c):  #k는 재귀의 깊이(정류장 번호), d는 배터리, c는 교환 횟수
    global cnt
    if k+1+d>=N:  #k+1을 해준 이유는 문제에서는 1번 정류장 부터 시작하는데 코드는 0번 부터 시작하는 것으로 짰기 때문
        if cnt>c:
            cnt=c
    if c>cnt or k>=len(bat):
        return
    # 매 정류장에서는 선택지가 2개 뿐이다.
    if d>0:  #남은 배터리 용량이 있으면
        f(k+1,d-1,c)     #그냥 가거나
    f(k+1,bat[k]-1,c+1)  #교환하고 가거나


for tc in range(1,int(input())+1):
    tmp = list(map(int,input().split()))
    N = tmp[0]
    bat = tmp[1:]
    cnt = 987654321

    f(0,bat[0],0)
    print("#{} {}".format(tc,cnt))



#교수님 dp풀이
# for tc in range(1,int(input())+1):
#     arr = list(map(int,input().split()))
#     N = arr[0]
#     dp = [0xffffff]*(N+1)
#
#     for i in range(1,1+arr[1]+1):
#         dp[i]=0
#     for i in range(2,N): #2번 정류장 ~ N-1번까지
#         for j in range(i+1,i+arr[i]+1):
#             #i번 정류장에서 교체, i-->j
#             if j>N:
#                 break
#             if dp[j]>dp[i]+1:
#                 dp[j]=dp[i]+1
#
#     print("#{} {}".format(tc,dp[N]))
