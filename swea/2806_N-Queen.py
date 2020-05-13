import sys
sys.stdin=open("2806_input.txt","r")

# def queen_position(k,r):
#     global cnt
#     if len(rl)==N:
#         cnt+=1
#         return
#     else:
#         for i in range(r,N):
#             for j in range(N):
#                 flag = 0
#                 if i in rl or j in cl:
#                     continue
#                 for k in range(len(rl)):
#                     if abs(i - rl[k]) == abs(j - cl[k]):
#                         flag = 1
#                         break
#                 if flag:
#                     continue
#                 rl.append(i)
#                 cl.append(j)
#                 queen_position(k+1,i)
#                 rl.pop()
#                 cl.pop()
#
#
# for tc in range(1,int(input())+1):
#     N = int(input())
#     chess_board = [[0]*N for _ in range(N)]
#     cnt = 0
#     flag = 0
#     rl = []
#     cl = []
#
#     queen_position(0,0)
#     print("#{} {}".format(tc,cnt))


def nqueen(a):
    cnt = 0
    n = len(a)
    if n == N:
        return 1
    for i in range(N):
        for j in range(n):
            if i==a[j] or abs(n-j)==abs(i-a[j]):
                break
        else:
            cnt += nqueen(a+[i])
    return cnt
for t in range(int(input())):
    N = int(input())
    a=[]
    print(f"#{t+1} {nqueen(a)}")





def perm(k):
    global cnt
    if k == N:
        cnt += 1
    for i in range(N):
        if check[i]: continue
        flag[0] = False
        for j in range(k):
            if abs(k - j) == abs(i - ans[j]):
                flag[0] = True
                break
        if flag[0]:
            continue

        check[i] = True
        ans.append(i)
        perm(k + 1)
        ans.pop()
        check[i] = False


tc = int(input())
for t in range(tc):
    N = int(input())
    check = [False] * N
    ans = []
    flag = [False]
    cnt = 0
    perm(0)
    print('#{} {}'.format(t + 1, cnt))