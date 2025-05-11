from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        num_words_per_users = defaultdict(int)
        ans = ""
        max_cnt = 0
        for i in range(len(messages)):
            num_words_per_users[senders[i]] += len(messages[i].split())
            if num_words_per_users[senders[i]] > max_cnt:
                max_cnt = num_words_per_users[senders[i]]
                ans = senders[i]
            elif num_words_per_users[senders[i]] == max_cnt:
                if ans < senders[i]:
                    ans = senders[i]

        return ans