class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        combinations = set()
        visited = [0] * len(tiles)
        def recur(n, k, string):
            if n == k:
                if string:
                    combinations.add(string)
                return

            for i in range(len(tiles)):
                if visited[i] == 1:
                    continue

                visited[i] = 1
                recur(n, k+1, string + tiles[i])
                recur(n, k+1, string)
                visited[i] = 0

        recur(len(tiles), 0, "")

        return len(combinations)


# best practice
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        print(tiles)
        if len(tiles)==1:
            return 1
        seen = set()
        ans = 0
        for indx,char in enumerate(tiles):
            seen.add(char)
            ans += 1 + self.numTilePossibilities(tiles[:indx]+tiles[indx+1:])
        return ans