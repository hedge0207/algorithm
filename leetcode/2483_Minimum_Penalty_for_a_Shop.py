class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_sum = [0] * (len(customers)+1)
        prefix_sum[0] = 0
        for i in range(len(customers)):
            num = 1 if customers[i] == "N" else 0
            prefix_sum[i+1] = num + prefix_sum[i]

        suffix_sum = [0] * (len(customers)+1)
        for i in range(len(customers)-1, -1, -1):
            num = 1 if customers[i] == "Y" else 0
            if i == len(customers)-1:
                suffix_sum[i] = num
            else:
                suffix_sum[i] = num + suffix_sum[i+1]

        min_penalty = float("inf")
        ans = 0
        for i in range(len(customers)+1):
            if min_penalty > prefix_sum[i] + suffix_sum[i]:
                min_penalty = prefix_sum[i] + suffix_sum[i]
                ans = i
        return ans



# best_practice
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        min_penalty = 0
        ans = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1

            if min_penalty > penalty:
                min_penalty = penalty
                ans = i + 1

        return ans
