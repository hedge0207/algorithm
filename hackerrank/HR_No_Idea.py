_ = input()
arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

ans = 0
for num in arr:
    if num in set_a:
        ans += 1
    if num in set_b:
        ans -= 1
print(ans)