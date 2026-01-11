class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        local_st, local_ed = points[0]
        for i in range(1, len(points)):
            st, ed = points[i]
            if local_st <= st <= local_ed:
                local_ed = min(local_ed, ed)
            else:
                ans += 1
                local_st, local_ed = st, ed
        ans += 1
        return ans



# best_practice
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        cur_end = points[0][1]

        for st, ed in points[1:]:
            if st > cur_end:
                arrows += 1
                cur_end = ed

        return arrows
