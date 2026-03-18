class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()
        max_cnt = 0
        for i in range(len(hBars)):
            for j in range(len(vBars)):
                h_i = i
                v_i = j
                pre_h_bar = hBars[h_i]
                pre_v_bar = vBars[v_i]
                diff = pre_h_bar - pre_v_bar
                h_i += 1
                v_i += 1
                cnt = 1
                while h_i < len(hBars) and v_i < len(vBars):
                    h_bar = hBars[h_i]
                    v_bar = vBars[v_i]
                    if diff != h_bar-v_bar:
                        break
                    if h_bar-1 != pre_h_bar or v_bar-1 != pre_v_bar:
                        break
                    cnt += 1
                    pre_h_bar, pre_v_bar = h_bar, v_bar
                    h_i += 1
                    v_i += 1
                max_cnt = max(max_cnt, cnt)
        return (max_cnt+1)**2



# best_practice
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()

        def find_continuous_chunk(nums) -> int:
            count = 1
            res = 0
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] - 1:
                    count += 1
                    res = max(res, count)
                else:
                    count = 1
            return max(res, count)

        h_count = find_continuous_chunk(hBars)
        v_count = find_continuous_chunk(vBars)
        return (min(h_count, v_count) + 1) ** 2