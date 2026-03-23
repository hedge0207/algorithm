class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_abs_diff = float("inf")
        ans = []
        for i in range(1, len(arr)):
            abs_diff = abs(arr[i-1]-arr[i])
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff
                ans = [[arr[i-1], arr[i]]]
            elif abs_diff == min_abs_diff:
                ans.append([arr[i-1], arr[i]])
        return ans