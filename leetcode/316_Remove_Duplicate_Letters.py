class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indices_per_char = {}
        for i in range(len(s)):
            char = s[i]
            if char in indices_per_char:
                indices_per_char[char].add(i)
            else:
                indices_per_char[char] = {i}

        ans = []
        for i in range(len(s)):
            char = s[i]
            indices_per_char[char].remove(i)
            if char in ans:
                continue
            while ans:
                post_char = ans[-1]
                if ord(post_char) > ord(char) and indices_per_char[post_char]:
                    ans.pop()
                else:
                    break
            ans.append(char)
        return "".join(ans)