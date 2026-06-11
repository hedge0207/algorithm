n = int(input())
sticks = sorted(list(map(int, input().split())))
median = sticks[n//2]
ans = sum([abs(stick-median) for stick in sticks])
print(ans)