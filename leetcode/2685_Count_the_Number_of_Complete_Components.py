from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_y > root_x:
            self.parent[root_y] = root_x
        elif root_y < root_x:
            self.parent[root_x] = root_y


class Solution:

    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        union_find = UnionFind(n)
        for s, t in edges:
            union_find.union(s, t)

        num_vertex_per_subgraph = defaultdict(int)
        for parent in union_find.parent:
            num_vertex_per_subgraph[union_find.find(parent)] += 1

        num_edges_per_subgraph = defaultdict(int)
        for s, _ in edges:
            num_edges_per_subgraph[union_find.find(s)] += 1

        ans = 0
        for root in num_vertex_per_subgraph:
            num_complete_edges = num_vertex_per_subgraph[root]*(num_vertex_per_subgraph[root]-1)//2
            if num_edges_per_subgraph[root] == num_complete_edges:
                ans += 1
        return ans