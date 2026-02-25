class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        ans = 0
        is_sorted = [0] * (len(strs)-1)
        for i in range(len(strs[0])):
            is_valid = True
            for j in range(len(strs)-1):
                if is_sorted[j] == 0 and strs[j][i] > strs[j+1][i]:
                    ans += 1
                    is_valid = False
                    break

            if not is_valid:
                continue

            for j in range(len(strs)-1):
                if is_sorted[j] == 0 and strs[j][i] < strs[j+1][i]:
                    is_sorted[j] = 1

            if all(is_sorted):
                break

        return ans