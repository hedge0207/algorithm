N = int(input())
arr = list(map(int, input().split()))

nge = []
stack = []
max_num = 0

for i in arr[::-1]:
    is_get_nge = False
    if i > max_num:
        stack = []
        max_num = i
    while len(stack) != 0:
        if stack[-1] > i:
            is_get_nge = True
            nge.append(stack[-1])
            break
        else:
            stack.pop()
    stack.append(i)
    if not is_get_nge:
        nge.append(-1)

for i in nge[::-1]:
    print(i, end=" ")
