from collections import Counter

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        all_counter = Counter(tops+bottoms)

        candidates = []
        n = len(tops)
        for num, cnt in all_counter.items():
            if cnt >= n:
                candidates.append(num)

        ans = -1
        for num in candidates:
            cnt = 0
            for top, bottom in zip(tops, bottoms):
                if top == num:
                    continue
                else:
                    if bottom != num:
                        break
                    cnt += 1
            else:
                if ans == -1:
                    ans = min(cnt, n-cnt)
                else:
                    ans = min(cnt, n-cnt, ans)

            cnt = 0
            for top, bottom in zip(tops, bottoms):
                if bottom == num:
                    continue
                else:
                    if top != num:
                        break
                    cnt += 1
            else:
                if ans == -1:
                    ans = min(cnt, n-cnt)
                else:
                    ans = min(cnt, n-cnt, ans)

        return ans


# best_practice
def minDominoRotations(tops: list[int], bottoms: list[int]) -> int:
    def check(x: int) -> int:
        rotation_top = rotation_bottom = 0
        for i in range(len(tops)):
            if tops[i] != x and bottoms[i] != x:
                return -1
            elif tops[i] != x:
                rotation_top += 1
            elif bottoms[i] != x:
                rotation_bottom += 1
        return min(rotation_top, rotation_bottom)

    # 전체 tops 또는 bottoms가 같은 값이 되도록 만들어야 하는데, 이때 각 도미노는 한 번만 회전 가능하다.
    # 따라서 가능한 숫자 후보는 오직 첫 번째 도미노의 두 숫자뿐이다:
    candidates = [tops[0], bottoms[0]]
    for candidate in candidates:
        result = check(candidate)
        if result != -1:
            return result
    return -1