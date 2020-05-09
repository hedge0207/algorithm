import sys
sys.stdin=open("4408_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time = 1
    stu = []
    for i in range(N):
        stu.append(list(map(int, input().split())))

    room=[0]*401
    for i in stu:
        a = (i[0]+1)//2
        b = (i[1]+1)//2
        if a>b:
            a,b=b,a
        for i in range(a,b+1):
            room[i]+=1

    print("#{} {}".format(tc,max(room)))