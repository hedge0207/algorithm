class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        today = 0
        for st, ed in meetings:
            if ed <= today:
                continue
            elif st > today:
                days -= ed - st + 1
            else:
                days -= ed - today
            today = ed
        return days