class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += 0 if happiness[i] - i <= 0 else happiness[i] - i
        return ans
