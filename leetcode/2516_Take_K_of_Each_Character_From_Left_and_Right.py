class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0, 0, 0]
        for char in s:
            cnt[ord(char)-97] += 1

        for num in cnt:
            if num < k:
                return -1

        st = 0
        max_size = 0
        for ed in range(len(s)):
            cnt[ord(s[ed]) - ord('a')] -= 1
            while cnt[ord(s[ed]) - ord('a')] < k:
                cnt[ord(s[st]) - ord('a')] += 1
                st += 1
            max_size = max(max_size, ed - st + 1)
        return len(s) - max_size