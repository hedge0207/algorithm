import sys
sys.stdin = open("5207_input.txt", 'r')

# 재귀
def binary_search(st, ed, t, c):
    global index, cnt
    if st > ed:
        return

    m = (st + ed) // 2

    if t == A[m]:
        cnt += 1
        return

    elif t < A[m] and c != 2:
        binary_search(st, m - 1, t, 2)

    elif t > A[m] and c != 1:
        binary_search(m + 1, ed, t, 1)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    A.sort()

    for i in B:
        binary_search(0, len(A) - 1, i, 0)
    print("#{} {}".format(tc, cnt))










# 반복
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     cnt = 0
#     A.sort()
#     for i in B:
#         st,ed=0,N-1
#         pre,cur = -1,0
#         while st<=ed and pre != cur:
#             prev = cur
#             m = (st+ed)//2
#             if A[m]==i:
#                 cnt+=1
#                 break
#             elif A[m]>i:
#                 ed,cur=m-1,1
#             else:
#                 st,cur=m+1,2
#     print("#{} {}".format(tc,cnt))
