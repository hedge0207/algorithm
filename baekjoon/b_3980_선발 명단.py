def f(k,s):
    global Max
    if k==11:
        Max = max(Max,s)
        return
    for i in range(11):
        if stat[k][i]==0 or selection[i]!=0:
            continue
        selection[i]=1
        f(k+1,s+stat[k][i])
        selection[i]=0



for tc in range(int(input())):
    stat = [list(map(int,input().split())) for _ in range(11)]
    selection = [0]*11
    Max = 0
    f(0,0)
    print(Max)