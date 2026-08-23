class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        nums.sort()
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        ans = 1
        if 1 in nums:
            length = cnt.pop(1)
            ans = length-1 if length % 2 == 0 else length


        for num in cnt.keys():
            length = 1
            cnt[num] -= 1
            while num * num in cnt and cnt[num] >= 1:
                cnt[num] -= 1
                num **= 2
                length += 2
                cnt[num] -= 1
            ans = max(ans, length)
        return ans