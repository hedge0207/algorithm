class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        ans = 0
        min_idx_per_color = {}
        for i in range(len(colors)):
            color = colors[i]
            if min_idx_per_color.get(color) is None:
                min_idx_per_color[color] = i
            for diff_col, idx in min_idx_per_color.items():
                if diff_col == color:
                    continue
                ans = max(i-idx, ans)
        return ans


# best_practice
def maxDistance(colors: list[int]) -> int:
    n = len(colors)
    ans = 0

    # Case 1: 왼쪽 끝(index 0)과 다른 색인 가장 먼 집 (오른쪽에서 탐색)
    for i in range(n - 1, -1, -1):
        if colors[i] != colors[0]:
            ans = max(ans, i)  # i - 0 = i
            break

    # Case 2: 오른쪽 끝(index n-1)과 다른 색인 가장 먼 집 (왼쪽에서 탐색)
    for i in range(n):
        if colors[i] != colors[n - 1]:
            ans = max(ans, n - 1 - i)
            break

    return ans