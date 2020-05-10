import sys
sys.stdin=open("5986_input.txt","r")

for tc in range(1,int(input())+1):
    N = int(input())

    pl = [2]
    for i in range(3, N):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            pl.append(i)

    cnt=0
    for i in range(len(pl)):
        for j in range(i,len(pl)):
            Sum = pl[i]+pl[j]
            if Sum>=N:
                break
            for k in range(j,len(pl)):
                Sum = pl[i] + pl[j]+pl[k]
                if Sum==N:
                    cnt+=1
                    break
                elif Sum>=N:
                    break
    print("#{} {}".format(tc,cnt))



# 재귀로 풀려 했으나 시간 초과
# def f(k,s,e):
#     global cnt
#     if k==3:
#         if s==N:
#             cnt+=1
#         return
#     elif s>=N:
#         return
#     else:
#         for i in range(2,N):
#             flag=1
#             for j in range(2,i):
#                 if i%j==0:
#                     flag=0
#             if flag or i==2:
#                 if i>=e:
#                     f(k+1,s+i,i)
#
#
# for tc in range(1,int(input())+1):
#     N = int(input())
#
#     cnt=0
#     f(0,0,0)
#     print("#{} {}".format(tc,cnt))

