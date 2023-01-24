N = int(input())
M = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

st, ed, ans = 0, N-1, 0

while st < ed:
    sum_ = ingredients[st] + ingredients[ed]
    if sum_ == M:
        ans += 1
        ed -= 1
        st += 1
    elif sum_ > M:
        ed -= 1
    else:
        st += 1

print(ans)
