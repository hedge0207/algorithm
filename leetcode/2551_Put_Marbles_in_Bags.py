class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        min_ = weights[0] + weights[-1]
        max_ = weights[0] + weights[-1]
        sum_ = []

        for i in range(1, len(weights)):
            sum_.append(weights[i-1] + weights[i])

        sum_.sort()
        if k != 1:
            max_ += sum(sum_[-k+1:])
            min_ += sum(sum_[:k-1])

        return max_ - min_