class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x:(x[0],x[1]))
        result = []
        st, ed = intervals[0]
        for i in range(1, len(intervals)):
            n_st, n_ed = intervals[i]

            if n_st > ed:
                result.append([st, ed])
                st= n_st

            if n_ed > ed:
                ed = n_ed

        result.append([st, ed])

        return result


# best practice
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[-1])
        return result