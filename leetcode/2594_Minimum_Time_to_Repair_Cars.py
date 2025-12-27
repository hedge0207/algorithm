import math

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        st, ed = 0, max(ranks)*cars**2 + 1
        while st < ed:
            mid = (st + ed) // 2
            repaired_cars = sum(int(math.sqrt(mid / r)) for r in ranks)
            if repaired_cars < cars:
                st = mid+1
            else:
                ed = mid
        return st