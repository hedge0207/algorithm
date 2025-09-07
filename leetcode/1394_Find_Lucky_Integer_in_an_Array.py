class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        ans = -1
        for num, cnt in counter.items():
            if num == cnt:
                if num > ans:
                    ans = num
        return ans

