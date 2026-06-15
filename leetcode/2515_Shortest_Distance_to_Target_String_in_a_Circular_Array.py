class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        indices = []
        for i, word in enumerate(words):
            if word == target:
                indices.append(i)

        if len(indices) == 0:
            return -1

        ans = float("inf")
        for i in indices:
            ans = min(ans, len(words) - abs(i - startIndex), abs(i-startIndex))
        return ans