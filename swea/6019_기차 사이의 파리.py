import sys
sys.stdin=open("6019_input.txt","r")

for tc in range(1,int(input())+1):
    D,A,B,F = map(int,input().split())
    ans = D*F/(A+B)
    print("#{} {:.10f}".format(tc,ans))


