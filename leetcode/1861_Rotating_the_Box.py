class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        new_grid = []
        for i in range(len(boxGrid)-1, -1, -1):
            num_stone = 0
            row = boxGrid[i]
            bottom = len(row)
            new_row = []
            for j in range(len(row)-1, -1, -1):
                if row[j] == "#":
                    num_stone += 1
                if row[j] == "*":
                    new_row += ["#"] * num_stone
                    new_row += ["."] * (bottom - j -1 - num_stone)
                    bottom = j
                    num_stone = 0
                    new_row.append("*")
            new_row += ["#"] * num_stone
            new_row += ["."] * (bottom + 1 - 1 - num_stone)
            new_grid.append(new_row)

        ans = []
        for i in range(len(boxGrid[0])-1, -1, -1):
            ans.append([new_grid[j][i] for j in range(len(boxGrid))])
        return ans