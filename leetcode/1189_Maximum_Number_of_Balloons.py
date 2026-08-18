from math import ceil

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in balloon:
                balloon[char] += 1

        ans = float("inf")
        for char, cnt in balloon.items():
            if char == "l" or char == "o":
                cnt = ceil(cnt // 2)
            ans = min(cnt, ans)
        return ans