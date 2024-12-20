def solution(k, tangerine):
    cnt = {}
    for size in tangerine:
        if cnt.get(size):
            cnt[size] += 1
        else:
            cnt[size] = 1
    cnt = dict(sorted(cnt.items(), key=lambda k: k[1], reverse=True))
    sum_ = 0
    ans = []
    for key, value in cnt.items():
        sum_ += value
        ans.append(key)
        if sum_ >= k:
            break
    return len(ans)