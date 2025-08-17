class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        is_k_dist = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == key:
                is_k_dist[i] = 1
                for j in range(1, k+1):
                    if i-j >= 0:
                        is_k_dist[i-j] = 1
                    if i + j < len(nums):
                        is_k_dist[i+j] = 1

        return [i for i in range(len(nums)) if is_k_dist[i]]