class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        n = len(words)
        is_removed = [0] * n
        idx1 = 0
        for idx2 in range(1, n):
            if sorted(words[idx1]) == sorted(words[idx2]):
                is_removed[idx2] = 1
            else:
                idx1 = idx2
        ans = []
        for i in range(n):
            if is_removed[i] == 0:
                ans.append(words[i])
        return ans