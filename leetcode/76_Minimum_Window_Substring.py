from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        for char in t:
            target[char] += 1

        source = {key:value for key, value in target.items()}
        st = 0
        ans = ""
        for ed in range(len(s)):
            if source.get(s[ed]) is not None:
                source[s[ed]] -= 1
            while st <= ed:
                flag = False
                for num in source.values():
                    if num > 0:
                        flag = True
                        break
                if flag:
                    break
                if source.get(s[st]) is not None:
                    if source[s[st]] + 1 > 0:
                        if ans:
                            if len(ans) > len(s[st:ed+1]):
                                ans = s[st:ed+1]
                        else:
                            ans = s[st:ed+1]
                        break
                    source[s[st]] += 1
                st += 1
        return ans