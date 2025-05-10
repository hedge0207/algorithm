class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in range(j+1, n):
                    if abs(arr[j]-arr[k]) > b or abs(arr[i]-arr[k]) > c:
                        continue
                    ans += 1

        return ans