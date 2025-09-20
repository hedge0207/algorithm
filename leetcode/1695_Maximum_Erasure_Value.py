class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        num_set = set()
        sum_ = 0
        ans = 0
        st = 0
        for ed in range(len(nums)):
            if nums[ed] in num_set:
                ans = max(ans, sum_)
                while 1:
                    num = nums[st]
                    num_set.remove(num)
                    sum_ -= num
                    st += 1
                    if num == nums[ed]:
                        break
            num_set.add(nums[ed])
            sum_ += nums[ed]
        ans = max(ans, sum_)
        return ans













s = Solution()
print(s.maximumUniqueSubarray([4,2,4,5,6]))
print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
print(s.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))

