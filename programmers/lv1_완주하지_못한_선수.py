def solution(participant, completion):
    players = {}
    for p in participant:
        if players.get(p) is None:
            players[p] = 1
        else:
            players[p] += 1

    for c in completion:
        if c not in players:
            return c
        players[c] -= 1

    for p, n in players.items():
        if n != 0:
            return p