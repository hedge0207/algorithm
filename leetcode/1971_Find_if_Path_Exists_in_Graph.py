class Solution:

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x

        for edge in edges:
            union(*edge)

        return find(source) == find(destination)





































s = Solution()
print(s.validPath(6, [[0,1], [0, 2], [3, 5], [5,4], [4,3]], 0, 5))
print(s.validPath(3, [[0,1], [1, 2], [2, 0]], 0, 2))