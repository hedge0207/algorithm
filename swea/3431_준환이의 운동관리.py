import sys
sys.stdin=open("3431_input.txt","r")

for tc in range(1,int(input())+1):
    L,U,X = map(int,input().split())
    if L<=X<=U:
        ans = 0
    elif X<L:
        ans=L-X
    else:
        ans=-1
    print("#{} {}".format(tc,ans))
