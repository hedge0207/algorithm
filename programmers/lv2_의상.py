from collections import defaultdict


def solution(clothes):
    clothes_per_type = defaultdict(set)
    ans = 1
    for name, type_ in clothes:
        clothes_per_type[type_].add(name)

    for v in clothes_per_type.values():
        ans *= len(v)+1
    return ans-1