from collections import defaultdict


class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited[node] = 1
            components_s[source[node]] += 1
            components_t[target[node]] += 1
            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue
                dfs(neighbor)

        n = len(source)
        ans = n
        visited = [0] * n
        for i in range(n):
            components_s = defaultdict(int)
            components_t = defaultdict(int)
            if visited[i]:
                continue
            dfs(i)
            for component, cnt in components_s.items():
                ans -= min(cnt, components_t[component])

        for i in range(n):
            if visited[i]:
                continue
            if source[i] == target[i]:
                ans -= 1

        return ans