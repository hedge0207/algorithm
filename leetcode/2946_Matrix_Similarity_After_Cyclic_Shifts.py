class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        for i in range(len(mat)):
            new_row = []
            for j in range(len(mat[i])):
                if i % 2:
                    new_j = (j - k) % len(mat[i])
                else:
                    new_j = (j + k) % len(mat[i])
                new_row.append(mat[i][new_j])
            if new_row != mat[i]:
                return False
        return True