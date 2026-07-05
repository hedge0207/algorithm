class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = {}
        for d in moves:
            if cnt.get(d):
                cnt[d] += 1
            else:
                cnt[d] = 1

        return abs(cnt.get("R", 0)-cnt.get("L", 0)) + cnt.get("_", 0)