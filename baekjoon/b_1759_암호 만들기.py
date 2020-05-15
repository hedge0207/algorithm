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
        while j<len(password):
            if password[j] not in ascv:
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
ascv = []
for i in strr:
    asc.append(ord(i))
for i in vowels:
    ascv.append(ord(i))

asc.sort()

f(0,0)




#개선한 코드
# def f(c,password):
#     if len(password)==L:
#         cnt = 0
#         for i in password:
#             if i in vowels:
#                 cnt+=1
#         if 0<cnt<len(password)-1:  #이렇게 할 수 있다는 것을 생각하지 못했다.
#             print(password)        #나는 각기 반복문을 돌려서 풀었다.
#
#     else:
#         for i in range(c,C):
#             f(i+1,password+strr[i])
#
# L,C = map(int,input().split())
# strr = sorted(list(input().split())) #문자열도 정렬이 된다. 나는 이걸 모르고 정렬을 위해 아스키 코드로 변환했다.
# vowels = ['a','e','i','o','u']
#
# f(0,'')
