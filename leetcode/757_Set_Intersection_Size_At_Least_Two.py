class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = [intervals[0][-1]-1, intervals[0][-1]]
        for i in range(1, len(intervals)):
            post_st, post_ed = ans[-2], ans[-1]
            st, ed = intervals[i]
            if st <= post_st:
                continue
            if st <= post_ed:
                ans.append(ed)
            else:
                ans.append(ed-1)
                ans.append(ed)
        return len(ans)