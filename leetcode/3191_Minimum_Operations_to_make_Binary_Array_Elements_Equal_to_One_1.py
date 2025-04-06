class Solution:
    def minOperations(self, nums: list[int]) -> int:
        slide_width = 3

        answer = 0
        for i in range(len(nums)-slide_width+1):
            if nums[i] == 0:
                answer += 1
                for j in range(i, i + slide_width):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0

        if all(nums):
            return answer
        else:
            return -1