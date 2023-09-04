class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        i = 0
        result = [0, 1]
        for j in range(2, n + 1):
            if j % 2 == 0:
                i += 1
                result.append(result[i])
            else:
                result.append(result[i] + result[i + 1])

        return max(result)
