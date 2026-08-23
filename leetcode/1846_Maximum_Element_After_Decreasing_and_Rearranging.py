class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        ans = 0
        for i in range(len(arr)):
            if arr[i] == ans:
                ans = arr[i]
            elif arr[i] > ans:
                ans += 1
            else:
                return ans

        return ans



# best_practice
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        target = 1
        for v in arr:
            if v >= target:
                target += 1
        return target - 1