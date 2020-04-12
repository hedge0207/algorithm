import sys
sys.stdin = open("1225_input.txt","r")

for _ in range(1,11):
    tc = int(input())
    pn = list(map(int, input().split()))
    password = pn
    mi = 0
    cnt = 0
    p = 0
    while p == 0:
        if cnt%5 == 0:
            mi = 0
        cnt += 1
        mi+=1
        a = password[0]-mi
        for i in range(1,len(password)):
            password[i-1]=password[i]
        password[-1]=a
        for i in range(len(password)):
            if password[i] <= 0:
                password[i] = 0
                p = 1

    result = ""
    for i in password:
        result += str(i)+" "
    print("#{} {}".format(tc,result))




