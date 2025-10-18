class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        ans = 0
        for i in range(n):
            top = points[i][1]
            bottom = -1
            for j in range(i+1, n):
                y = points[j][1]
                if bottom < y <= top:
                    ans += 1
                    bottom = y
                    if top == bottom:
                        break
        return ans