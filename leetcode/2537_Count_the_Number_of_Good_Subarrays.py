from collections import defaultdict

class Solution:
    def get_num_pairs(self, n: int) -> int:
        return n * (n - 1) // 2 if n >= 2 else 0

    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        num_pairs = 0
        ans = 0
        st = 0

        for ed in range(n):
            num_pairs -= self.get_num_pairs(counter[nums[ed]])
            counter[nums[ed]] += 1
            num_pairs += self.get_num_pairs(counter[nums[ed]])

            while num_pairs >= k:
                ans += n - ed
                num_pairs -= self.get_num_pairs(counter[nums[st]])
                counter[nums[st]] -= 1
                num_pairs += self.get_num_pairs(counter[nums[st]])
                st += 1

        return ans