import sys
sys.stdin=open("9700_input.txt","r")

for tc in range(1,int(input())+1):
    p,q = map(float,input().split())
    if (1-p)*q<p*(1-q)*q:
        print("#{} YES".format(tc))
    else:
        print("#{} NO".format(tc))