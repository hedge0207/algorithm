n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for student, apple in arr:
    ans += apple % student
print(ans)