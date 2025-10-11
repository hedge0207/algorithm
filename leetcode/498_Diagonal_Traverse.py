class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        i = 0
        j = 0
        for _ in range(m * n):
            ans.append(mat[i][j])

            if (i + j) % 2 == 0:
                if j == n - 1:
                    i += 1
                else:
                    if i == 0:
                        j += 1
                    else:
                        i -= 1
                        j += 1
            else:
                if i == m-1:
                    j += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        i += 1
                        j -= 1
        return ans













s = Solution()
# print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
# print(s.findDiagonalOrder([[1,2],[3,4]]))
