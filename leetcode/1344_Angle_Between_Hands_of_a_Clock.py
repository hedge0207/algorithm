class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour % 12 * 30) + (minutes * 0.5)
        m = minutes * 6

        if abs(h-m) > 180:
            return 360-abs(h-m)
        return abs(h-m)
