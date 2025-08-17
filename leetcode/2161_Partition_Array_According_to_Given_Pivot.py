class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        same = []
        greater = []
        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                less.append(num)
            else:
                same.append(num)
        return less + same + greater

























s = Solution()
print(s.pivotArray([9,12,5,10,14,3,10], 10))
print(s.pivotArray([-3,4,3,2], 2))