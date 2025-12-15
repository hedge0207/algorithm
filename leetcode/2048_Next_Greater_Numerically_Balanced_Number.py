from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224445):
            count = Counter(str(i))
            for num, cnt in count.items():
                if int(num) != cnt:
                    break
            else:
                return i