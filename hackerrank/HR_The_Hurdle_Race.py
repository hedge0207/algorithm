def hurdleRace(k, height):
    max_ = max(height)
    if max_ - k >= 0:
        return max_ - k
    else:
        return 0