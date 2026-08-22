def icecreamParlor(m, arr):
    seen = {}
    for i, cost in enumerate(arr):
        complement = m - cost
        if complement in seen:
            return [seen[complement] + 1, i + 1]
        seen[cost] = i