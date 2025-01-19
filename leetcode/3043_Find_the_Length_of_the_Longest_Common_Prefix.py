class Solution:

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        suffixes = set()
        for num in arr2:
            suffix = ""
            for char in num:
                suffix += char
                suffixes.add(suffix)

        result = 0
        for num in arr1:
            suffix = ""
            for char in num:
                suffix += char
                if suffix in suffixes:
                    result = max(result, len(suffix))

        return result