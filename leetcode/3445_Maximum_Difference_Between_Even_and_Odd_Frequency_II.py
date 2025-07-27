# 결국 못 풀었다.
from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        nums = list(map(int, s))
        prefix_count = {}
        freq = defaultdict(int)
        for i in range(n):
            num = nums[i]
            freq[num] += 1
            if prefix_count.get(num) is None:
                prefix_count[num] = [0] * n

            for key in prefix_count:
                prefix_count[key][i] = freq[key]

        prefix_lst = [prefix_cnt_lst for prefix_cnt_lst in prefix_count.values()]
        ans = float("-inf")
        def find_max_diff(st, ed):
            nonlocal ans

            max_odd_freq = float("-inf")
            min_even_freq = float("inf")
            for prefix in prefix_lst:
                if st == 0:
                    num = prefix[ed]
                else:
                    num = prefix[ed] - prefix[st-1]
                if num == 0:
                    continue
                if num % 2 == 0:
                    min_even_freq = min(min_even_freq, num)
                else:
                    max_odd_freq = max(max_odd_freq, num)

            ans = max(ans, max_odd_freq - min_even_freq)

        for i in range(n):
            for j in range(i+2, n):
                if j-i < k-1:
                    continue
                find_max_diff(i, j)

        return ans


# solution
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = float("-inf")
        for a in "01234":
            for b in "01234":
                if a != b:
                    seen = defaultdict(lambda : float("inf"))
                    pa = [0]
                    pb = [0]
                    ii = 0
                    for i, ch in enumerate(s):
                        pa.append(pa[-1])
                        pb.append(pb[-1])
                        if ch == a: pa[-1] += 1
                        elif ch == b: pb[-1] += 1
                        while ii <= i-k+1 and pa[ii] < pa[-1] and pb[ii] < pb[-1]:
                            key = (pa[ii] % 2, pb[ii] % 2)
                            diff = pa[ii] - pb[ii]
                            seen[key] = min(seen[key], diff)
                            ii += 1
                        key = (1 - pa[-1] % 2, pb[-1] % 2)
                        diff = pa[-1] - pb[-1]
                        ans = max(ans, diff - seen[key])
        return ans