class Spreadsheet:

    def __init__(self, num_rows: int):
        self._rows = [[0]*26 for _ in range(num_rows)]

    def _get_coordinate(self, cell) -> list[int]:
        return [ord(cell[0])-65, int(cell[1:])-1]

    def setCell(self, cell: str, value: int) -> None:
        x, y = self._get_coordinate(cell)
        self._rows[y][x] = value

    def resetCell(self, cell: str) -> None:
        x, y = self._get_coordinate(cell)
        self._rows[y][x] = 0

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula.split("+")
        cell1 = cell1[1:]
        try:
            num1 = int(cell1)
        except ValueError:
            x, y = self._get_coordinate(cell1)
            num1 = self._rows[y][x]

        try:
            num2 = int(cell2)
        except ValueError:
            x, y = self._get_coordinate(cell2)
            num2 = self._rows[y][x]

        return num1 + num2