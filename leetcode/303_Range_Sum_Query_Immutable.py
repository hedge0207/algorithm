class NumArray:
    def __init__(self, nums: list[int]):
        self._nums = nums
        self._sum = [0]
        for num in nums:
            self._sum.append(self._sum[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum[right+1] - self._sum[left]