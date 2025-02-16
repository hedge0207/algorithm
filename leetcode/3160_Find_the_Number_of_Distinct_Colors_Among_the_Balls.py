class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        balls = {ball_num: 0 for ball_num, _ in queries}
        num_distinct_color = 0
        counter = {}

        result = []
        for ball, color in queries:
            prev_color = balls[ball]
            if prev_color != 0:
                counter[prev_color] -= 1
                if counter[prev_color] == 0:
                    num_distinct_color -= 1
            if counter.get(color):
                counter[color] += 1
            else:
                counter[color] = 1
            balls[ball] = color
            if counter[color] == 1:
                num_distinct_color += 1
            result.append(num_distinct_color)
        return result