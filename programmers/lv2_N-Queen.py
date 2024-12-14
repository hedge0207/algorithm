class NQueen:
    def __init__(self):
        self.ans = 0

    def backtrack(self, n, x, positions):
        if x == n:
            if len(positions) == n:
                self.ans += 1
            return

        for j in range(n):
            possible = False
            for position in positions:
                if position[1] == j or abs(position[0] - x) == abs(position[1] - j):
                    break
            else:
                possible = True
            if possible:
                positions.append([x, j])
                self.backtrack(n, x + 1, positions)
                positions.pop()


def solution(n):
    nqueen = NQueen()
    nqueen.backtrack(n, 0, [])
    return nqueen.ans