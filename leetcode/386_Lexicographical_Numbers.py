class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = [str(i) for i in range(1, n+1)]
        return list(map(int, sorted(ans)))
