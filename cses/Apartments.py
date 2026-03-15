n, m, k = map(int, input().split())
applicants = sorted(list(map(int, input().split())))
apartments = sorted(list(map(int, input().split())))

ans = 0
apart_i = 0
for i in range(n):
    while apart_i < m and applicants[i] > apartments[apart_i] + k:
        apart_i += 1

    if apart_i == m:
        break

    if apartments[apart_i] - k <= applicants[i] <= apartments[apart_i] + k:
        ans += 1
        apart_i += 1
        continue
print(ans)