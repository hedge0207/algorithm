class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = 0
        sum_ = 0
        for num in gain:
            sum_ += num
            ans = max(ans, sum_)
        return ans
