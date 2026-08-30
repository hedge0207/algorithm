class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        id_per_node = {}
        graph = set()
        ed = 0
        id_ = 0
        for st in range(n):
            if st not in graph:
                id_ += 1
                id_per_node[st] = id_
                graph = {st}
            while ed < n:
                if nums[ed] - nums[st] > maxDiff:
                    break
                id_per_node[ed] = id_
                graph.add(ed)
                ed += 1

        ans = []
        for i, j in queries:
            if id_per_node[i] == id_per_node[j]:
                ans.append(True)
            else:
                ans.append(False)
        return ans