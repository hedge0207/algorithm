from collections import deque

N, K = map(int, input().split())

circle = [i for i in range(1, N + 1)]
queue = deque()
answer = []

for num in circle:
    queue.append(num)

idx = 0
while queue:
    if len(queue) == 1:
        answer.append(queue[0])
        break
    for i in range(K):
        if i == K-1:
            answer.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print("<", end="")
for idx in range(len(answer)):
    if idx == len(answer)-1:
        print(answer[idx], end="")
    else:
        print(answer[idx], end=", ")
print(">", end="")
