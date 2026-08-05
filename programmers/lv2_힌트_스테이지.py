from collections import defaultdict


def solution(cost, hint):
    n = len(cost)
    answer = float("inf")
    def recur(d, total, bundle_per_stage):
        nonlocal answer

        if d == n:
            answer = min(answer, total)
            return

        new_bundle = defaultdict(int)
        recur(d+1, total+cost[d][min(bundle_per_stage[d+1], n-1)], bundle_per_stage)
        if d < len(hint):
            for i in range(1, len(hint[d])):
                new_bundle[hint[d][i]] += 1
            for stage, cnt in new_bundle.items():
                bundle_per_stage[stage] += cnt
            recur(d+1, total+cost[d][min(bundle_per_stage[d+1], n-1)]+hint[d][0], bundle_per_stage)
            for stage, cnt in new_bundle.items():
                bundle_per_stage[stage] -= cnt
    recur(0, 0, defaultdict(int))

    return answer