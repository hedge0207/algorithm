class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
        costs = []
        for i in range(max_cost+1):
            costs += [i]*count[i]
        ans = 0
        for cost in costs:
            coins -= cost
            if coins >= 0:
                ans += 1
            else:
                break
        return ans


s = Solution()
print(s.maxIceCream([1,3,2,4,1],
7))