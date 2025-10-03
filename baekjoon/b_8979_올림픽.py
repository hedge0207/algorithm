n, target = map(int, input().split())

medals_per_counties = []
for i in range(n):
    medals_per_counties.append(list(map(int, input().split())))

medals_per_counties.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 1
cnt = 0
post_ = []
for i in range(n):
    if post_ and medals_per_counties[i][1:] == post_:
        cnt += 1
    else:
        rank += cnt
        cnt = 1
        post_ = medals_per_counties[i][1:]
    if medals_per_counties[i][0] == target:
        print(rank)
        break































"""
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1

4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0

2 2
1 1 0 0
2 0 1 0
"""