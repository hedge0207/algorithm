import sys

N = int(sys.stdin.readline())
buildings = list(int(sys.stdin.readline()) for _ in range(N))

stack = [[buildings[-1], 0]]
cnt = 0

for i in range(N - 2, -1, -1):
    t_cnt = 0
    flag = True
    while len(stack) != 0 and buildings[i] > stack[-1][0]:
        t_cnt += stack.pop()[-1] + 1

    stack.append([buildings[i], t_cnt])
    cnt += t_cnt

print(cnt)

# 틀린 코드
# N = int(input())
# buildings = list(int(input()) for _ in range(N))
#
# stack = [[buildings[-1], 0]]
# cnt = 0
#
# for i in range(N - 2, -1, -1):
#     t_cnt = 0
#     flag = True
#     while len(stack) != 0 and buildings[i] > stack[-1][0]:
#         if flag and stack[-1][-1] != 0:
#             t_cnt += stack[-1][-1]+1
#             flag = False
#         else:
#             t_cnt += 1
#         stack.pop()
#
#     stack.append([buildings[i], t_cnt])
#     cnt += t_cnt
#
#
# print(cnt)