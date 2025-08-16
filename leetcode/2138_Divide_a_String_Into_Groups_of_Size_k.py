class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        ans = []
        for i in range(0, len(s), k):
            sub_string = s[i:i+k]
            sub_string += fill * (k-len(sub_string))
            ans.append(sub_string)
        return ans