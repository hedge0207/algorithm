import sys

sys.stdin = open("4047_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    cards = input()

    # cd = {"s": 0, "d": 0, "h": 0, "c": 0}
    cls=[]
    cld=[]
    clh=[]
    clc=[]
    flag=True

    for i in range(0,len(cards),3):
        a=""
        if cards[i]=="S":
            a+=cards[i+1]+cards[i+2]
            if a in cls:
                flag=False
                break
            cls.append(a)
        if cards[i]=="D":
            a+=cards[i+1]+cards[i+2]
            if a in cld:
                flag=False
                break
            cld.append(a)
        if cards[i]=="H":
            a+=cards[i+1]+cards[i+2]
            if a in clh:
                flag=False
                break
            clh.append(a)
        if cards[i]=="C":
            a+=cards[i+1]+cards[i+2]
            if a in clc:
                flag=False
                break
            clc.append(a)
    result=[]
    result.append(cls)
    result.append(cld)
    result.append(clh)
    result.append(clc)


    if flag:
        print("#{}".format(tc),end=" ")
        for i in range(4):
            print(13-len(result[i]),end=" ")
        print()
    else:
        print("#{} ERROR".format(tc))




dicta = {"a":0,"b":1}
a = dicta["a"]
print(a)








