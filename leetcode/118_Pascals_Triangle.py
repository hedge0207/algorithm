class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        def cur(nums):
            result.append(nums)

            if len(nums) == numRows:
                return

            new_nums = []
            new_nums.append(1)
            for i in range(len(nums)//2):
                new_nums.append(nums[i] + nums[i+1])
            if len(nums) % 2:
                new_nums += new_nums[::-1]
            else:
                new_nums += new_nums[-2::-1]
            cur(new_nums)

        cur([1])
        return result