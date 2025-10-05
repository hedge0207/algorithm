class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        is_occupied = [0] * len(baskets)
        for fruit in fruits:
            for i in range(len(baskets)):
                if is_occupied[i]:
                    continue
                if baskets[i] >= fruit:
                    is_occupied[i] = 1
                    break
        return is_occupied.count(0)