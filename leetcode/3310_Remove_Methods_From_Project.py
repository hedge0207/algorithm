class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = {}
        for caller, callee in invocations:
            if graph.get(caller):
                graph[caller].append(callee)
            else:
                graph[caller] = [callee]

        suspicious_methods = {k}
        visited = [0] * n
        visited[k] = 1
        def find_suspicious_methods(node):
            if graph.get(node) is None:
                return

            for callee in graph[node]:
                if visited[callee]:
                    continue
                visited[callee] += 1
                suspicious_methods.add(callee)
                find_suspicious_methods(callee)
        find_suspicious_methods(k)

        non_suspicious_methods = set(i for i in range(n)) - suspicious_methods
        for method in non_suspicious_methods:
            if graph.get(method) is None:
                continue
            for callee in graph[method]:
                if callee in suspicious_methods:
                    return [i for i in range(n)]

        ans = []
        for i in range(n):
            if i in suspicious_methods:
                continue
            ans.append(i)
        return ans