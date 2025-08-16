class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        coordinates_of_zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    coordinates_of_zero.append([i, j])

        for coordinate in coordinates_of_zero:
            y, x = coordinate
            for i in range(len(matrix[0])):
                matrix[y][i] = 0
            for i in range(len(matrix)):
                matrix[i][x] = 0


























s = Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
