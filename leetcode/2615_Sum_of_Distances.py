class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        indices_per_num = {}
        for i in range(len(nums)):
            num = nums[i]
            if indices_per_num.get(num):
                indices_per_num[num].append(i)
            else:
                indices_per_num[num] = [i]

        ans = [0] * len(nums)
        for indices in indices_per_num.values():
            for i in range(1, len(indices)):
                idx, before_idx = indices[i], indices[i-1]
                ans[idx] += ans[before_idx] + (idx - before_idx)*i

            suffix_sum = 0
            for i in range(len(indices)-2, -1, -1):
                idx, before_idx = indices[i], indices[i+1]
                suffix_sum += (before_idx - idx) * (len(indices)-1-i)
                ans[idx] += suffix_sum
        return ans