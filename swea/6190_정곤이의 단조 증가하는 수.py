import sys
sys.stdin=open("6190_input.txt","r")

for tc in range(1,int(input())+1):
    N = int(input())
    number = list(map(int,input().split()))

    Max = -1
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            num = str(number[i]*number[j])
            if len(num)==1:
                continue
            else:
                flag = 1
                for k in range(len(num)-1):
                    if num[k]>num[k+1]:
                        flag=0
                if flag:
                    Max = max(int(num),Max)
    print("#{} {}".format(tc,Max))