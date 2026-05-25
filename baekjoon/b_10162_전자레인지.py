n = int(input())
buttons = [300, 60, 10]
ans = []
for button in buttons:
    ans.append(n // button)
    n %= button
if n == 0:
    print(" ".join(map(str, ans)))
else:
    print(-1)