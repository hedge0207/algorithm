class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        for row in board:
            nums = set()
            for num in row:
                if num == ".":
                    continue
                if num in nums:
                    return False
                nums.add(num)

        for i in range(9):
            nums = set()
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                if num in nums:
                    return False
                nums.add(num)

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                nums = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num == ".":
                            continue
                        if num in nums:
                            return False
                        nums.add(num)
        return True
