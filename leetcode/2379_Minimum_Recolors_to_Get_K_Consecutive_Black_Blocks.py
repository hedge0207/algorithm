class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        num_white = 0
        for i in range(k):
            if blocks[i] == "W":
                num_white += 1

        ans = min(num_white, ans)
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                num_white += 1
            if blocks[i-k] == "W":
                num_white -= 1
            ans = min(num_white, ans)
        return ans