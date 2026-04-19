from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        company = defaultdict(list)
        for i in range(len(manager)):
            company[manager[i]].append(i)
        ans = 0
        def dfs(node, sum_):
            nonlocal ans
            if company.get(node) is None:
                ans = max(ans, sum_)
                return

            for next_node in company[node]:
                dfs(next_node, sum_ + informTime[node])
        dfs(headID, 0)
        return ans