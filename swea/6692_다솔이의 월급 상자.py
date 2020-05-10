import sys
sys.stdin=open("6692_input.txt","r")

for tc in range(1,int(input())+1):
    N = int(input())
    ans = 0
    for i in range(N):
        a,b = input().split()
        sal = float(a)*int(b)
        ans+=sal
    print("#{} {:.6f}".format(tc,ans))
