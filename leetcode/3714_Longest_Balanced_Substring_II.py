class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        run = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run += 1
            else:
                run = 1
            ans = max(ans, run)

        a = b = c = 0
        first = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            state = (a - b, a - c)
            if state in first:
                ans = max(ans, i - first[state])
            else:
                first[state] = i

        def best_two_chars(excluded: str) -> int:
            best = 1
            diff = 0
            earliest = {0: -1}

            def update_diff(ch: str) -> int:
                nonlocal diff
                if excluded == 'c':
                    if ch == 'a':
                        diff += 1
                    elif ch == 'b':
                        diff -= 1
                elif excluded == 'b':
                    if ch == 'a':
                        diff += 1
                    elif ch == 'c':
                        diff -= 1
                else:
                    if ch == 'b':
                        diff += 1
                    elif ch == 'c':
                        diff -= 1
                return diff

            for i, ch in enumerate(s):
                if ch == excluded:
                    diff = 0
                    earliest = {0: i}
                    continue

                d = update_diff(ch)
                if d in earliest:
                    best = max(best, i - earliest[d])
                else:
                    earliest[d] = i

            return best

        ans = max(ans, best_two_chars('a'))
        ans = max(ans, best_two_chars('b'))
        ans = max(ans, best_two_chars('c'))

        return ans