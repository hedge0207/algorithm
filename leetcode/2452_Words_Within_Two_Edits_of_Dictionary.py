class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        ans = []
        for query in queries:
            for word in dictionary:
                diff = sum(q_char != w_char for q_char, w_char in zip(query, word))
                if diff <= 2:
                    ans.append(query)
                    break
        return ans