class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty_bottles = numBottles
        while empty_bottles // numExchange:
            ans += empty_bottles // numExchange
            empty_bottles = empty_bottles // numExchange + empty_bottles % numExchange
        return ans