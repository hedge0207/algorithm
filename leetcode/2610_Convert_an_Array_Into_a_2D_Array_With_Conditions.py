class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        cnt = {}
        ans = [[]]
        for num in nums:
            idx = 0
            if cnt.get(num):
                cnt[num] += 1
                idx = cnt[num] - 1
            else:
                cnt[num] = 1
            if len(ans) > idx:
                ans[idx].append(num)
            else:
                ans.append([num])
        return ans