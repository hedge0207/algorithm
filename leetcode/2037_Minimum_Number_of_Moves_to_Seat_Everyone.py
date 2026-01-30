class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for seat, student in zip(seats, students):
            ans += abs(seat - student)
        return ans