class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                idx = i
                break
        if idx == -1:
            return True

        dist = 0
        for i in range(idx+1, len(nums)):
            if nums[i] == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
        return True