class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        arr = [0]
        n = len(differences)
        for i in range(n):
            arr.append(differences[i]+arr[-1])
        ans = upper - (max(arr) + lower-min(arr)) + 1
        if ans < 0:
            return 0
        return ans
