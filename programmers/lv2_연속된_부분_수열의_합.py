def solution(sequence, k):
    ans = []
    ed = 0
    sum_ = sequence[0]
    for st in range(len(sequence)):
        while sum_ < k and ed < len(sequence)-1:
            ed += 1
            sum_ += sequence[ed]
        if sum_ == k:
            if ans:
                if ed - st < ans[1]-ans[0]:
                    ans = [st, ed]
            else:
                ans = [st, ed]
        sum_ -= sequence[st]

    return ans