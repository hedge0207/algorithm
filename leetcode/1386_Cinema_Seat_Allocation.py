class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reservedSeats.sort()
        seats1 = [1, 2, 3, 4]
        seats2 = [3, 4, 5, 6]
        seats3 = [5, 6, 7, 8]
        ans = n * 2
        pre_row = -1
        seat_row = [0, 0, 0]
        for row, column in reservedSeats:
            row -= 1
            column -= 1
            if pre_row != row:
                if seat_row[0] == 0 and seat_row[2] == 0:
                    pass
                elif all(seat_row):
                    ans -= 2
                else:
                    ans -= 1
                seat_row = [0, 0, 0]
                pre_row = row
            if column in seats1:
                seat_row[0] = 1
            if column in seats2:
                seat_row[1] = 1
            if column in seats3:
                seat_row[2] = 1

        if seat_row[0] == 0 and seat_row[2] == 0:
            pass
        elif all(seat_row):
            ans -= 2
        else:
            ans -= 1

        return ans
