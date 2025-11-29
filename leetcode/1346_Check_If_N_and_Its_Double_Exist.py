class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums = {}
        for num in arr:
            if nums.get(num):
                nums[num] += 1
            else:
                nums[num] = 1

        for num, cnt in nums.items():
            if num * 2 in nums:
                if num * 2 == num and cnt == 1:
                    continue
                return True
        return False
