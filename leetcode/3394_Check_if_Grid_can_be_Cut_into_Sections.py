class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        order_by_x = sorted(rectangles, key=lambda x: (x[0], -x[2]))
        order_by_y = sorted(rectangles, key=lambda x: (x[1], -x[3]))
        x_chunks = []
        y_chunks = []

        for i in range(len(rectangles)):
            x_st, x_ed = order_by_x[i][0], order_by_x[i][2]
            y_st, y_ed = order_by_y[i][1], order_by_y[i][3]

            if len(x_chunks) == 0 or x_chunks[-1][1] <= x_st:
                x_chunks.append([x_st, x_ed])
            else:
                x_chunks[-1][1] = max(x_ed, x_chunks[-1][1])

            if len(y_chunks) == 0 or y_chunks[-1][1] <= y_st:
                y_chunks.append([y_st, y_ed])
            else:
                y_chunks[-1][1] = max(y_ed, y_chunks[-1][1])

        return len(x_chunks) >= 3 or len(y_chunks) >= 3


































s = Solution()
print(s.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(s.checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(s.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))
