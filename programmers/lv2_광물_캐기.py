from enum import Enum


class Weight(Enum):
    diamond = 25
    iron = 5
    stone = 1


def solution(picks, minerals):
    answer = 0
    DURABILITY = 5
    limit = min(sum(picks)*DURABILITY, len(minerals))
    weight = []
    for i in range(0, limit, DURABILITY):
        tmp = [Weight[mineral].value for mineral in minerals[i:i+DURABILITY]]
        weight.append([sum(tmp), tmp])
    weight.sort(reverse=True, key=lambda x:x[0])

    weight_per_pick = {0: 25, 1: 5, 2: 1}
    for _, mineral_weight_lst in weight:
        pick_idx = 0
        for i in range(3):
            if picks[i] == 0:
                continue
            pick_idx = i
            picks[i] -= 1
            break

        for mineral_weight in mineral_weight_lst:
            answer += mineral_weight // weight_per_pick[pick_idx] or 1
    return answer