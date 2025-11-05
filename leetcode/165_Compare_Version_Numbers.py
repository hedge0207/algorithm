class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_lst = version1.split(".")
        ver2_lst = version2.split(".")

        n = len(ver1_lst)
        m = len(ver2_lst)
        i, j = 0, 0

        while i < n or j < m:
            v1 = 0
            if i < n:
                v1 = int(ver1_lst[i])
                i += 1

            v2 = 0
            if j < m:
                v2 = int(ver2_lst[j])
                j += 1

            if v1 > v2:
                return 1

            if v1 < v2:
                return -1
        return 0