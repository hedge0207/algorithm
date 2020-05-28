# import sys
# sys.stdin=open("2806_input.txt","r")

#내 풀이(아래에 더 나은 풀이가 존재)
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






#풀이 1
# def n_queen(row):    #재귀의 깊이가 행의 역할, 재귀의 깊이가 0이면 row는 0, 1이면 row는 1...이런 식이므로
#     global cnt       #행이 겹치는지는 따로 검사할 필요가 없다.
#     if row == N:
#         cnt += 1
#     for i in range(N):
#         if queen_column[i]:  #만일 같은 열에 퀸을 놓은 적 있으면
#             continue  #continue
#         flag = False
#         for j in range(row):
#             if abs(row - j) == abs(i - ans[j]):  #대각선 검사: (x,y)와 대각선 상에 있는 임의의 좌표(a,b)는
#                 flag = 1                         #항상 abs(x-a)==abs(y-b)가 성립한다.
#                 break                            #j는 0~row-1까지이므로 이전 행에 대한 정보이다.
#         if flag:                                 #ans[j]에는 이전 열에 대한 정보가 담겨 있다.
#             continue
#         queen_column[i] = 1  #열을 체크
#         ans.append(i)           #대각선 비교를 위해 열의 정보를 담아준다.
#         n_queen(row + 1)        #재귀를 통해 다음 열로 넘어간다
#         ans.pop()
#         queen_column[i] = 0
#
#
# tc = int(input())
# for t in range(tc):
#     N = int(input())
#     queen_column = [0] * N
#     ans = []
#     flag = 0
#     cnt = 0
#     n_queen(0)
#     print('#{} {}'.format(t + 1, cnt))




# #풀이 2
# #크기=n, 세로 =[y], 대각선 / = [x+y], 대각선 반대 ＼ = [x-y+n-1]
# n, ans = int(input()), 0
# a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1) #a=세로, b=대각선, c=대각선 반대
# #(2*n-1)는 x+y의 최댓값인 2*n-2에서+1을 해준 것
# #예를 들어 n=5일 때 x+y의 최댓값은 8이다(x,y는 0~4까지).
# #나올 수 있는 값은 총 9(0~8,2*n-1)가지
# #마찬가지로 x-y+n-1의 최대값 역시 8이고, 최소값은 0(x=0,y=4일 때)이다.
# #따라서 나올 수 있는 값은 0~8의 9가지
#
# def solve(i):  #재귀의 깊이가 행의 역할
#     global ans
#     if i == n:
#         ans += 1
#         return
#     for j in range(n):  #j는 열의 역할
#         if not (a[j] or b[i+j] or c[i-j+n-1]): #전부 false일 때만 아래 코드가 실행된다.
#             a[j] = b[i+j] = c[i-j+n-1] = True
#             solve(i+1)
#             a[j] = b[i+j] = c[i-j+n-1] = False
#
# solve(0)
# print(ans)
# #출처: https://rebas.kr/761 [PROJECT REBAS]