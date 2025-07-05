class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        answer = []
        for i, word in enumerate(words):
            for char in word:
                if x == char:
                    answer.append(i)
                    break
        return answer