import sys
sys.stdin=open("5203_input.txt",'r')

for tc in range(1,int(input())+1):
    cards = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    winner =0
    i = 0
    while i<12 and not winner:
        if i&1:
            p2[cards[i]]+=1
            if 3 in p2:
                winner = 2
            for j in range(len(p2)-2):
                if p2[j] and p2[j+1] and p2[j+2]:
                    winner = 2
        else:
            p1[cards[i]]+=1
            if 3 in p1:
                winner = 1
            for j in range(len(p1)-2):
                if p1[j] and p1[j+1] and p1[j+2]:
                    winner = 1
        i+=1
    print("#{} {}".format(tc,winner))




