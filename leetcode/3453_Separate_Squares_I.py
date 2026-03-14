class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        st = float("inf")
        ed = 0
        for x, y, l in squares:
            if y < st:
                st = y
            if y + l > ed:
                ed = y + l

        while st < ed:
            mid = (st + ed) / 2
            upper_sum = 0
            lower_sum = 0
            for x, y, l in squares:
                if y < mid < y+l:
                    upper_sum += (y+l-mid) * l
                    lower_sum += (mid-y) * l
                    continue
                if y + l <= mid:
                    lower_sum += l * l
                    continue
                if mid <= y:
                    upper_sum += l * l
                    continue
            old_st, old_ed = st, ed
            if upper_sum > lower_sum:
                st = mid
            else:
                ed = mid
            if old_st == st and old_ed == ed:
                break
        return round(ed, 5)