import sys

N = int(input())
stack = []
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == "push":
        stack.append(a[1])
    elif a[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print("-1")
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) != 0:
            print("0")
        else:
            print("1")
    else:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])


#아래와 같이 작성시 시간초과
# N = int(input())
# stack = []
# for _ in range(N):
#     a = list(input().split())
#     if a[0] == "push":
#         stack.append(a[1])
#     elif a[0] == "pop":
#         if len(stack) != 0:
#             print(stack.pop())
#         else:
#             print("-1")
#     elif a[0] == "size":
#         print(len(stack))
#     elif a[0] == "empty":
#         if len(stack) != 0:
#             print("0")
#         else:
#             print("1")
#     else:
#         if len(stack) == 0:
#             print("-1")
#         else:
#             print(stack[-1])


