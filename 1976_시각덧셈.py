import sys
sys.stdin=open("1976_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    t1,m1,t2,m2 = map(int, input().split())

    a = t1+t2
    b = m1+m2
    if a > 12:
        a -= 12
    if b >= 60:
        b -= 60
        a += 1
    print("#{} {} {}".format(tc,a,b))