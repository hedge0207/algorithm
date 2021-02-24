# 시간 초과
# 1<=N<=500000이하

# N = int(input())
# buildings = list(map(int, input().split()))
# result = []
# for i in range(N - 1, -1, -1):
#     tmp = 0
#     for j in range(i - 1, -1, -1):
#         if buildings[j] >= buildings[i]:
#             tmp = j + 1
#             break
#     result.append(tmp)
#
# for i in range(N - 1, -1, -1):
#     print(result[i], end=" ")


# 스택 활용 시간 단축
N = int(input())
buildings = list(map(int, input().split()))
stack = [[1, buildings[0]]]
idx = [0]
for i in range(1, N):
    flag = False
    while stack:
        if stack[-1][-1] < buildings[i]:
            stack.pop()
        else:
            break
        if len(stack) == 0:
            flag = True

    if flag:
        idx.append(0)
    else:
        idx.append(stack[-1][0])

    if i != len(buildings) - 1:
        stack.append([i + 1, buildings[i]])

for i in idx:
    print(i, end=" ")
