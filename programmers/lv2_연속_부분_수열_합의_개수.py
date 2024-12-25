def solution(elements):
    sum_subset = set()
    n = len(elements)
    for length in range(1, n + 1):
        for i in range(n):
            if length + i - n >= 0:
                sum_subset.add(sum(elements[i:] + elements[:length + i - n]))
            else:
                sum_subset.add(sum(elements[i:i + length]))
    return len(sum_subset)