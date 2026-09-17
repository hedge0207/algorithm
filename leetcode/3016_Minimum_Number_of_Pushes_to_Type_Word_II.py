class Solution:
    def minimumPushes(self, word: str) -> int:
        num_per_char = {}
        for char in word:
            if char in num_per_char:
                num_per_char[char] += 1
            else:
                num_per_char[char] = 1

        nums = sorted(num_per_char.values(), reverse=True)

        ans = 0
        for i in range(len(nums)):
            ans += (i // 8 + 1) * nums[i]
        return ans