class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        hFences += [1, m]
        vFences += [1, n]
        hFences.sort()
        vFences.sort()
        h_diff = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                h_diff.add(hFences[j] - hFences[i])
        v_diff = set()
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                v_diff.add(vFences[j] - vFences[i])
        if len(h_diff.intersection(v_diff)) == 0:
            return -1
        else:
            return max(h_diff.intersection(v_diff))**2 % (10**9+7)