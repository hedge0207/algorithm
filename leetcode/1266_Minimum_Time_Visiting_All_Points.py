class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        ans = 0
        cur_x, cur_y = points[0]
        for next_x, next_y in points[1:]:
            ans += max(abs(next_y-cur_y), abs(next_x-cur_x))
            cur_x, cur_y = next_x, next_y
        return ans