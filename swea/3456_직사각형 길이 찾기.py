import sys
sys.stdin=open("3456_input.txt","r")

for tc in range(1,int(input())+1):
    a,b,c = map(int,input().split())
    ans = 0
    if a==b:
        ans = c
    elif a==c:
        ans=b
    else:
        ans=a
    print("#{} {}".format(tc,ans))
