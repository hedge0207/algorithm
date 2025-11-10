class Solution:
    def maxArea(self, height: list[int]) -> int:
        st, ed = 0, len(height)-1
        ans = 0
        while st < ed:
            cur_water = min(height[ed], height[st]) * (ed - st)
            ans = max(ans, cur_water)

            if height[ed] > height[st]:
                st += 1
            else:
                ed -= 1
        return ans