class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        last_num = float("-inf")
        for num in nums:
            max_ = num + k
            min_ = num - k
            if min_ > last_num:
                last_num = min_
            else:
                last_num += 1

            if last_num <= max_:
                ans += 1
            else:
                last_num -= 1
        return ans