class Robot:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._cur_idx = 0
        self._perimeter = 2 * (width + height) - 4
        self._moved = False

    def _get_pos_by_idx(self):
        if self._cur_idx < self._width - 1:
            return [self._cur_idx, 0]
        elif self._cur_idx < (self._width - 1) + (self._height - 1):
            return [
                self._width - 1,
                self._cur_idx - (self._width - 1)
            ]
        elif self._cur_idx < (self._width - 1) + (self._height - 1) + (self._width - 1):
            return [
                self._width - 1 - (
                    self._cur_idx - (self._width - 1) - (self._height - 1)
                ),
                self._height - 1
            ]
        else:
            return [
                0,
                self._height - 1 - (
                    self._cur_idx
                    - (self._width - 1)
                    - (self._height - 1)
                    - (self._width - 1)
                )
            ]

    def step(self, num: int) -> None:
        if num > 0:
            self._moved = True
        self._cur_idx = (self._cur_idx + num) % self._perimeter

    def getPos(self):
        return self._get_pos_by_idx()

    def getDir(self):
        if self._cur_idx == 0:
            return "East" if not self._moved else "South"
        elif self._cur_idx <= self._width - 1:
            return "East"
        elif self._cur_idx <= (self._width - 1) + (self._height - 1):
            return "North"
        elif self._cur_idx <= (self._width - 1) * 2 + (self._height - 1):
            return "West"
        else:
            return "South"