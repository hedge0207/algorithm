from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        map = defaultdict(lambda: defaultdict(list))
        for l, r, top in allowed:
            map[l][r].append(top)

        def combination(n, candidates, sub_string, result):
            if len(sub_string) == n:
                if sub_string:
                    result.append(sub_string)
                return

            for char in candidates[len(sub_string)]:
                combination(n, candidates, sub_string + char, result)

        ans = False

        def recur(row):
            nonlocal ans

            if ans:
                return

            if len(row) == 1:
                ans = True
                return

            row_candidates = []
            for i in range(len(row) - 1):
                if map[row[i]] and map[row[i]][row[i + 1]]:
                    row_candidates.append(map[row[i]][row[i + 1]])
                else:
                    break

            if len(row_candidates) < len(row)-1:
                return

            possible_rows = []
            combination(len(row)-1, row_candidates, "", possible_rows)
            for possible_row in possible_rows:
                recur(possible_row)

        recur(bottom)
        return ans