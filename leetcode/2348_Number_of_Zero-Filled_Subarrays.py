class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        nums.append(-1)
        len_sub_array = []
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                if cnt != 0:
                    len_sub_array.append(cnt)
                cnt = 0

        memo = {}
        ans = 0
        for length in len_sub_array:
            if memo.get(length) is None:
                memo[length] = sum([i for i in range(1, length+1)])
            ans += memo[length]

        return ans