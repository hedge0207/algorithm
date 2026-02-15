class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        min_i, max_i, min_j, max_j = 0, len(matrix)-1, 0, len(matrix[0])-1
        while 1:
            for j in range(min_j, max_j+1):
                ans.append(matrix[min_i][j])
            min_i += 1
            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for i in range(min_i, max_i+1):
                ans.append(matrix[i][max_j])
            max_j -= 1
            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for j in range(max_j, min_j-1, -1):
                ans.append(matrix[max_i][j])
            max_i -= 1
            if len(ans) == len(matrix) * len(matrix[0]):
                break

            for i in range(max_i, min_i-1, -1):
                ans.append(matrix[i][min_j])
            min_j += 1
            if len(ans) == len(matrix) * len(matrix[0]):
                break
        return ans