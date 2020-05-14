#미완
def f(k,c):
    if k==L:
        flag1=0
        flag2=0
        for i in vowels:
            if ord(i) in password:
                flag1 = 1
                break
        cnt = 0
        j = 0
        while j<5:
            if ord(vowels[j]) not in password:
                cnt+=1
            if cnt>=2:
                flag2=1
                break
            j+=1
        if flag1 and flag2:
            for i in range(len(password)):
                print(chr(password[i]),end="")
            print()
        return
    for i in range(c,C):
        if visited[i] == 0:
            visited[i]=1
            password.append(asc[i])
            f(k+1,i)
            password.pop()
            visited[i]=0


L,C = map(int,input().split())
strr = list(input().split())
vowels = ['a','e','i','o','u']
visited = [0]*C
password = []

asc = []
for i in strr:
    asc.append(ord(i))

asc.sort()

f(0,0)