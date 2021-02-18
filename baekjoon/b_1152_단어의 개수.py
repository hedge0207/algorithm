words = input()

cnt=0
for i in range(len(words)):
    if words[i]==' ' and i != 0 and i != len(words)-1:
        cnt+=1

if words==' ':
    print(0)
else:
    print(cnt + 1)

