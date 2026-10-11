m, d = map(int, input().split())
s = input()
watched = [0] * m

for i in range(m):
    if s[i] == "G":
        for j in range(max(0, i-d), min(m, i+d+1)):
            watched[j] = 1

ans = 0
for i in range(m):
    if watched[i] == 0:
        ans += 1
print(ans)