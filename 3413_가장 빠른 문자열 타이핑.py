# import sys
# sys.stdin = open("3143_input.txt", "r")
# 오답 코드
# 반례: aaaab aaab
# 아래와 같은 코드로는 애초에 풀 수 없었다.
# T = int(input())
# for tc in range(1, T + 1):
#     A, B = input().split()
#     idx = 0
#     cnt = 0
#     N = len(A)
#     M = len(B)
#     for i in range(N):
#         if A[i] == B[idx]:
#             idx += 1
#             if idx == len(B):
#                 cnt += 1
#                 idx = 0
#             else:
#                 continue
#         else:
#             idx = 0
#
#     print("#{} {}".format(tc, N - M * cnt + cnt))


# T = int(input())
# for tc in range(1, T + 1):
#     A, B = input().split()
#     i = 0
#     cnt = 0
#     N = len(A)
#     M = len(B)
#     while i<=N-M:
#         j = 0
#         while j<M and A[i+j]==B[j]:
#             j+=1
#         if j==M:
#             cnt+=1
#             i+=M
#         else:
#             i+=1
#     print("#{} {}".format(tc, N - M * cnt + cnt))
