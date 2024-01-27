from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == "+":
                record.append(record[-1] + record[-2])
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "C":
                record.pop()
            else:
                record.append(int(operation))

        return sum(record)


s = Solution()
s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
