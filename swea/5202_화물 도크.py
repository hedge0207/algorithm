import sys
sys.stdin=open("5202_input.txt","r")

for tc in range(1,int(input())+1):
    N = int(input())
    dock = []
    for i in range(N):
        dock.append(list(map(int,input().split())))

    #끝나는 순서대로 정렬하고 앞 타임의 가장 빨리 끝나는 것과 다음 타임에 가장 빨리 시작하는 것을 비교하면 된다.
    #탐욕 알고리즘, 위와 같은 선택을 연속적으로 하면 최적해를 찾을 수 있다.
    dock.sort(key=lambda x: x[1])
    cnt = 1
    a = 0
    for i in range(1,N):
        if dock[i][0]>=dock[a][1]:
            a = i
            cnt+=1

    print("#{} {}".format(tc,cnt))

