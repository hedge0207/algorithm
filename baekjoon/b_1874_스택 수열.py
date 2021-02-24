n = int(input())
lst = [int(input()) for _ in range(n)]
stack = []
result = ''
num = 1
idx = 0

while idx < n:
    if len(stack) != 0 and stack[-1] == lst[idx]:
        stack.pop()
        idx += 1
        result += '-'
    elif num <= n:
        stack.append(num)
        num += 1
        result += "+"
    else:
        break

if stack:
    print("NO")
else:
    for i in result:
        print(i)