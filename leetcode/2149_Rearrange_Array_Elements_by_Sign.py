class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
        ans = []
        for p, n in zip(pos, neg):
            ans += [p, n]
        return ans