import sys

input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
    word = input().rstrip()
    stack = [word[0]]
    for char in word[1:]:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if len(stack) == 0:
        cnt += 1

print(cnt)