def solution(n, cities, budget):
    sum_ = sum(cities)
    if budget >= sum_:
        return max(cities)
    st, ed = 0, budget
    ans = 0
    while st <= ed:
        mid = (st+ed) // 2
        sum_ = 0
        for city in cities:
            if city <= mid:
                sum_ += city
            else:
                sum_ += mid
            if sum_ > budget:
                ed = mid-1
                break
        else:
            ans = max(ans, mid)
            st = mid + 1
    return ans

print(solution(int(input()), list(map(int, input().split())), int(input())))