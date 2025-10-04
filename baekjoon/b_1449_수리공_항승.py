N, L = map(int, input().split())
leaked_positions = sorted(list(map(int, input().split())))

ans = 1
sum_ = 1
for i in range(1, N):
    sum_ += leaked_positions[i] - leaked_positions[i-1]
    if sum_ <= L:
        continue
    else:
        ans += 1
        sum_ = 1
print(ans)

























"""
4 2
1 2 100 101

4 3 
1 2 3 4

6 5
1 2 3 4 5 6

3 1
3 2 1
"""