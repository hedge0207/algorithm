class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for i in range(len(str1)):
            if str2[j] == str1[i] or str2[j] == chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')):
                j += 1
            if j == len(str2):
                return True
        return False