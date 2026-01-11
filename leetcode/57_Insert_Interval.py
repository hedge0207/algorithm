class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        ans = []
        local_st, local_ed = intervals[0]
        for i in range(1, len(intervals)):
            st, ed = intervals[i]
            if local_st <= st <= local_ed:
                local_ed = max(local_ed, ed)
            else:
                ans.append([local_st, local_ed])
                local_st, local_ed = st, ed
        ans.append([local_st, local_ed])

        return ans