class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = "abc"
        candidates = []
        def recur(happy_string):
            if len(candidates) >= k:
                candidates.append(happy_string)
                return

            if n == len(happy_string):
                candidates.append(happy_string)
                return

            for char in chars:
                if happy_string and happy_string[-1] == char:
                    continue
                recur(happy_string + char)
        recur("")
        return candidates[k-1] if len(candidates)>=k else ""