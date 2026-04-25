class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort(reverse=True)
        st, ed = 1, piles[0]
        while st < ed:
            mid = (st+ed) // 2
            take_time = 0
            for pile in piles:
                take_time += pile // mid
                if pile % mid:
                    take_time += 1
                if take_time > h:
                    break
            if take_time > h:
                st = mid + 1
            else:
                ed = mid
        return st
