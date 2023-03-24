import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        def dfs(before):
            if before in check:
                return False

            if before in result:
                return True

            check.add(before)
            for i in graph[before]:
                if not dfs(i):
                    return False

            check.remove(before)

            result.add(before)

            return True

        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])


        result = set()
        check = set()
        for after in list(graph):
            if not dfs(after):
                return False

        return True