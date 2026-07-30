class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        if len(cost) < 3:
            return sum(cost)

        ans = 0
        for i in range(len(cost)):
            if (i+1) % 3 == 0:
                continue
            ans += cost[i]
        return ans
