from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(from_, path):
            if graph.get(from_) is None:
                if len(path)-1 == len(tickets):
                    result.append(path)
                    return -1
                return

            flag = True
            for idx, to_ in enumerate(graph[from_]):
                graph[from_][idx] = None
                if to_ is None:
                    continue
                flag = False
                v = dfs(to_, path + [to_])
                if v != -1:
                    graph[from_][idx] = to_
                else:
                    return -1

            if flag and len(path)-1 == len(tickets):
                result.append(path)
                return -1


        graph = {}
        for from_, to in tickets:
            if graph.get(from_):
                graph[from_].append(to)
            else:
                graph[from_] = [to]

        for v in graph.values():
            v.sort()

        result = []
        dfs("JFK", ["JFK"])

        return result[0]


# best practice
import collections

def findItinerary(tickets):
    graph = collections.defaultdict(list)
    for from_, to in sorted(tickets):
        graph[from_].append(to)

    route = []

    def dfs(from_):
        while graph[from_]:
            dfs(graph[from_].pop(0))
        route.append(from_)

    dfs("JFK")
    return route[::-1]

findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])