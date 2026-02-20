class Solution:
    def maxLength(self, arr: list[str]) -> int:
        ans = 0
        def backtrack(unique_str, d):
            nonlocal ans
            if d == len(arr):
                return

            unique_set = set(unique_str)
            for i in range(d, len(arr)):
                char_set = set(arr[i])
                if len(arr[i]) != len(char_set):
                    continue
                if char_set & unique_set:
                    continue
                ans = max(len(unique_str+arr[i]), ans)
                backtrack(unique_str + arr[i], i+1)
        backtrack("", 0)
        return ans