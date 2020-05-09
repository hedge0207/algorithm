import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    num_l = []
    c = 1
    cnt = 0
    while len(num_l) != 10:
        cnt+=1
        num = N*c
        for i in str(num):
            if i not in num_l:
                num_l.append(i)
        c+=1
    print("#{} {}".format(tc, cnt*N))