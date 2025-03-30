class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000}
        nums = []
        for char in s[::-1]:
            if nums and nums[-1] > roman_to_int[char]:
                nums.append(-roman_to_int[char])
            else:
                nums.append(roman_to_int[char])
        return sum(nums)