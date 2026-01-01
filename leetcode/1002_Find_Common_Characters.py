from collections import defaultdict

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        total_cnt = defaultdict(int)
        for word in words:
            local_cnt = defaultdict(int)
            for char in word:
                local_cnt[char] += 1
            for char, cnt in local_cnt.items():
                for i in range(cnt):
                    total_cnt[char+str(i)] += 1
        return [char[0] for char, num in total_cnt.items() if num == len(words)]



