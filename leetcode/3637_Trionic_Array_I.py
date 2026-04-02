class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        is_inc = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            elif nums[i] > nums[i-1]:
                if len(is_inc)==0 or not is_inc[-1]:
                    is_inc.append(True)
                else:
                    continue
            else:
                if len(is_inc) == 0:
                    return False
                if is_inc[-1]:
                    is_inc.append(False)
                else:
                    continue

        return is_inc == [True, False, True]