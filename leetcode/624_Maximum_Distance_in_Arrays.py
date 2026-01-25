class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        max_values = sorted([[arrays[i][-1], i] for i in range(len(arrays))])
        min_values = sorted([[arrays[i][0], i] for i in range(len(arrays))])
        if max_values[-1][1] != min_values[0][1]:
            ans = abs(max_values[-1][0] - min_values[0][0])
        else:
            ans = max(abs(max_values[-2][0] - min_values[0][0]), abs(max_values[-1][0] - min_values[1][0]))
        return ans



# best_practice
class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        m = len(arrays)
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0
        for i in range(1, m):
            cur_smallest = arrays[i][0]
            cur_biggest = arrays[i][-1]
            max_distance = max(max_distance, abs(biggest-cur_smallest), abs(cur_biggest - smallest))
            smallest = min(smallest, cur_smallest)
            biggest = max(biggest, cur_biggest)
        return max_distance