class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        num_invalid = 0
        post_color = colors[0]
        for i in range(1, k):
            if colors[i] == post_color:
                num_invalid += 1
            post_color = colors[i]

        ans = 0
        if num_invalid == 0:
            ans += 1
        for i in range(n-1):
            next_i = (i+1) % n
            if colors[i] == colors[next_i]:
                num_invalid -= 1

            ed = (i+k) % n
            if colors[ed] == colors[(i-1+k) % n]:
                num_invalid += 1
            if num_invalid == 0:
                ans += 1
        return ans