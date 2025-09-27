class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        post_row = [1]
        ans = []
        for i in range(numRows):
            ans.append(post_row)
            next_row = [1]
            for i in range(len(post_row)-1):
                next_row.append(post_row[i]+post_row[i+1])
            next_row.append(1)
            post_row = next_row
        return ans


















s = Solution()
print(s.generate(5))