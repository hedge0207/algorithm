def solution(N, stages):
    stages.sort()
    num_per_stage = {i:0 for i in range(1, N+1)}
    for stage in stages:
        if num_per_stage.get(stage) is None:
            continue
        num_per_stage[stage] += 1
    total = len(stages)
    sum_ = 0
    fail_rate = {i:0 for i in range(1, N)}
    for k, v in num_per_stage.items():
        if total - sum_ > 0:
            fail_rate[k] = v / (total-sum_)
            sum_ += v
        else:
            fail_rate[k] = 0
    return [i[0] for i in sorted(fail_rate.items(), key=lambda x: (x[1], -x[0]), reverse=True)]