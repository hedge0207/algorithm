from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ed = len(numbers) - 1
        for i, num in enumerate(numbers):
            st = i + 1
            other_num = target - num

            while st <= ed:
                mid = (st + ed) // 2
                if numbers[mid] == other_num:
                    return [i + 1, mid + 1]
                elif numbers[mid] > other_num:
                    ed = mid - 1
                else:
                    st = mid + 1