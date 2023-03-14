class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}

        for stone in stones:
            if stone in freq:
                freq[stone] += 1
            else:
                freq[stone] = 1

        return sum([freq[jewel] for jewel in jewels if jewel in freq])