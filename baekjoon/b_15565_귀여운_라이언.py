N, K = map(int, input().split())
dolls = list(map(int, input().split()))

st = 0
num_lion = 0
position_lion = []
ans = float("inf")
for i in range(len(dolls)):
    if dolls[i] == 1:
        position_lion.append(i)
        num_lion += 1
        if num_lion >= K:
            ans = min(ans, position_lion[-1] - position_lion[-K] + 1)

if ans < float("inf"):
    print(ans)
else:
    print(-1)