class Solution:
    def _calculate_score(self, a_and_b, sup, sub, sup_s, sub_s):
        score = 0
        stack = []
        for a_or_b in a_and_b:
            if a_or_b == sub and stack and stack[-1] == sup:
                stack.pop()
                score += sup_s
            else:
                stack.append(a_or_b)

        new_stack = []
        for a_or_b in stack:
            if a_or_b == sup and new_stack and new_stack[-1] == sub:
                new_stack.pop()
                score += sub_s
            else:
                new_stack.append(a_or_b)

        return score

    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        sup, sub, sup_s, sub_s = "a", "b", x, y
        if x <= y:
            sup, sub, sup_s, sub_s = "b", "a", y, x
        a_and_b = []
        for char in s:
            if char not in ["a", "b"]:
                ans += self._calculate_score(a_and_b, sup, sub, sup_s, sub_s)
                a_and_b = []
            else:
                a_and_b.append(char)
        if len(a_and_b) >=2 :
            ans += self._calculate_score(a_and_b, sup, sub, sup_s, sub_s)
        return ans































s = Solution()
print(s.maximumGain("cdbcbbaaabab", 4, 5))
print(s.maximumGain("aabbaaxybbaabb", 5, 4))

"aabbaa""bbaabb"