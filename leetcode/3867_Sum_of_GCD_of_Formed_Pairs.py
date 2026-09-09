class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        max_ = 0
        for num in nums:
            if max_ < num:
                max_ = num
            a, b = max_, num
            while b != 0:
                a, b = b, a % b
            prefix_gcd.append(a)

        prefix_gcd.sort()
        ans = 0
        st, ed = 0, len(nums)-1
        while st < ed:
            a, b = prefix_gcd[ed], prefix_gcd[st]
            while b != 0:
                a, b = b, a % b
            ans += a
            st += 1
            ed -= 1
        return ans