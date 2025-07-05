from collections import defaultdict


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        word_dict = {}
        for word in words:
            if word_dict.get(word):
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        ans = 0
        center = False
        for word, cnt in word_dict.items():
            if cnt == 0:
                continue
            rev_word = word[::-1]
            if word_dict.get(rev_word) is None:
                continue

            if word == rev_word:
                ans += cnt // 2 * 4
                if not center and cnt % 2 == 1:
                    center = True
                    ans += 2
            else:
                ans += min(cnt, word_dict[rev_word]) * 4
            word_dict[word] = 0
            word_dict[rev_word] = 0
        return ans























s = Solution()
print(s.longestPalindrome(["lc","cl","gg"]))
print(s.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
print(s.longestPalindrome(["cc","ll","xx"]))
print(s.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))


