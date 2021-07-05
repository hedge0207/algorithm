N = int(input())
length = len(str(N))

start = -1
if N - 9*length > 0:
    start = N - 9 * length
else:
    start = 0

answer = 0
for num in range(start, N):
    if num + sum(map(int, str(num))) == N:
        answer = num
        break
print(answer)