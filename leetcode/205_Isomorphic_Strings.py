class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for a, b in zip(s, t):
            if a in s_to_t:
                if s_to_t[a] != b:
                    return False
            else:
                s_to_t[a] = b

            if b in t_to_s:
                if t_to_s[b] != a:
                    return False
            else:
                t_to_s[b] = a

        return True











s = Solution()
# print(s.isIsomorphic("badc","baba"))
print(s.isIsomorphic("paper","title"))
