class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        tmp = []
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                tmp.append([s[i-1], cnt])
                cnt = 0
            cnt += 1
        tmp.append([s[-1], cnt])
        max_ = 0
        max_idx = -2
        for i in range(1, len(tmp)-1):
            if tmp[i-1][0] == tmp[i+1][0] == "0" and tmp[i][0] == "1":
                sum_ = tmp[i-1][1] + tmp[i+1][1]
                if sum_ > max_:
                    max_ = sum_
                    max_idx = i

        ans = 0
        for i in range(len(tmp)):
            if tmp[i][0] == "1":
                ans += tmp[i][1]
            else:
                if i == max_idx - 1 or i == max_idx + 1:
                    ans += tmp[i][1]
        return ans



# best practice
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        # Pad with '1' to correctly capture boundary 0-runs
        padded_s = '1' + s + '1'

        # Extract only valid, non-empty 0-runs
        zero_runs = [len(run) for run in padded_s.split('1') if run]

        # If there are fewer than two valid 0-runs, no trade pattern is possible
        if len(zero_runs) < 2:
            return ones

        # Find the maximum sum of any two adjacent valid 0-runs
        best = max(zero_runs[i] + zero_runs[i + 1] for i in range(len(zero_runs) - 1))

        return ones + best