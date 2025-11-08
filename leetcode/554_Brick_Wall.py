class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        num_edges = {}
        for line in wall:
            idx = 0
            for i in range(len(line)-1):
                idx += line[i]
                if num_edges.get(idx):
                    num_edges[idx] += 1
                else:
                    num_edges[idx] = 1
        n = len(wall)
        if len(num_edges) == 0:
            return n
        else:
            return n - max(num_edges.values())