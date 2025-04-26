class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        table = [0]*(n+1)

        for i in range(n-1, -1, -1):
            points, brain_power = questions[i]
            next_points = 0
            if i+brain_power+1 < n:
                next_points = table[i+brain_power+1]
            table[i] = max(table[i+1], points + next_points)
            print(table)
        return table[0]
