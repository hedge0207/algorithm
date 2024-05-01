from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        for char in strs[0]:
            for word in strs:
                if len(word) <= i or word[i] != char:
                    break
            else:
                result += char
                i += 1
        
        return result

s = Solution()
s.longestCommonPrefix(["dog", "cat", "racecar"])
s.longestCommonPrefix(["flower", "flow", "flight"])
s.longestCommonPrefix(["flower", "flow", ""])
