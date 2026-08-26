class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:[x[0], -x[1]])
        print(intervals)
        removed = 0
        st, ed = intervals[0]
        for i in range(1, len(intervals)):
            nst, ned = intervals[i]
            if st <= nst and ned <= ed:
                removed += 1
                continue
            st, ed = nst, ned
        return len(intervals) - removed