from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    fields = ["lang", "job", "career", "food"]
    table = defaultdict(list)

    for detail in info:
        l, j, c, f, s = detail.split()
        score = int(s)
        values = {"lang": l, "job": j, "career": c, "food": f}

        for r in range(5):
            for combo in combinations(fields, r):
                key_dict = dict(values)
                for field in combo:
                    key_dict[field] = "-"
                key = tuple(key_dict[f] for f in fields)
                table[key].append(score)

    for key in table:
        table[key].sort()

    ans = []
    for q in query:
        tokens = q.split()
        key = (tokens[0], tokens[2], tokens[4], tokens[6])
        score_threshold = int(tokens[7])

        scores = table[key]
        idx = bisect_left(scores, score_threshold)
        ans.append(len(scores) - idx)

    return ans