n = int(input())

post = 1
cnt = 1
for i in range(2, n):
    cnt, post = cnt+post, cnt

print(cnt)