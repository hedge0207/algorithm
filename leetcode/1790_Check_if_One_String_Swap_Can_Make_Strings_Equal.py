class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx1 = -1
        diff_idx2 = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if diff_idx1 == -1:
                    diff_idx1 = i
                else:
                    diff_idx2 = i
        if diff_idx2 != -1:
            tmp = list(s2)
            tmp[diff_idx1], tmp[diff_idx2] = tmp[diff_idx2], tmp[diff_idx1]
            s2 = "".join(tmp)
        return s1 == s2