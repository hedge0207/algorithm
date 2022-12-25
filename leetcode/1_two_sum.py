from typing import List

# 단순한 문제이기는 하지만 최적화 할 수 있는 방법이 많아 배울 것이 많은 문제
# brute-force 풀이(O(n**2))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# in을 사용(O(n**2), 상수가 빠지는 시간복잡도의 특성상 위 풀이와 동일하지만 실제로는 더 빠르다)
# target에서 특정 숫자를 뺀 값이 nums 안에 있으면, 특정 숫자와 뺀 값을 반환한다.
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        complete = target - num

        if complete in nums[i+1:]:
            return [nums.index(num), nums[i+1:].index(complete) + (1+1)]


# dict 형태로 변경하여 index 조회 속도를 개선(O(n))
# 위 풀이들은 index를 사용하여 nums에서 index를 찾는 데 시간을 들여야 했다.
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 찾아야 하는 두 숫자 중 첫 번째 숫자를 찾으면, 두 번째 숫자도 바로 알 수 있다.
    for i, num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return [i, nums_map[target-num]]


# 위 코드에서 구조를 개선(시간복잡도는 동일, 코드만 간결해진다)
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i