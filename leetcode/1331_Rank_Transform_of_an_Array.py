class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return []

        sorted_arr = sorted(arr)
        num_rank_map = {}
        prev_num = sorted_arr[0]
        rank = 1
        num_rank_map[prev_num] = rank
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] != prev_num:
                rank += 1
                num_rank_map[sorted_arr[i]] = rank
                prev_num = sorted_arr[i]

        ans = []
        for num in arr:
            ans.append(num_rank_map[num])
        return ans


