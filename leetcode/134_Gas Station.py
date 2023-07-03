from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        sum_gas = sum(gas)
        sum_cost = sum(cost)

        if sum_cost > sum_gas:
            return -1

        result = 0
        fuel = 0
        for i in range(n):
            if gas[i] + fuel < cost[i]:
                fuel = 0
                result = i + 1
            else:
                fuel += gas[i] - cost[i]

        return result