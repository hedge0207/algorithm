n = int(input())
students = list(map(int, input().split()))
a, b = map(int, input().split())

ans = n
for student in students:
    student -= a
    if student <= 0:
        continue
    ans += student // b
    if student % b:
        ans += 1
print(ans)