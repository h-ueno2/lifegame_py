from random import randint


class CellData:
    data = []
    rows = 0
    cols = 0

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.clear()

    def clear(self):
        data2 = []
        for row in range(0, self.rows):
            data2.append([False for col in range(0, self.cols)])
        self.data = data2

    def create(self):
        data2 = []
        for row in range(0, self.rows):
            data2.append([(randint(0, 9) <= 2)
                          for col in range(0, self.cols)])
        self.data = data2

    def count_livingcells_around(self, row: int, col: int):
        # 周囲の生存セルを数える
        cnt = 0
        tbl = [(-1, -1), (0, -1), (1, -1), (1, 0),
               (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for t in tbl:
            check_col, check_row = [col + t[0], row + t[1]]
            if 0 <= check_col < self.cols and 0 <= check_row < self.rows:
                if self.data[check_row][check_col]:
                    cnt += 1
        return cnt

    def is_next_live(self, cell: bool, count: int):
        if count == 3:
            return True
        if cell:
            if 2 <= count <= 3:
                return True
            return False
        return cell

    def check(self, row, col):
        count = self.count_livingcells_around(row=row, col=col)
        return self.is_next_live(self.data[row][col], count)

    def next_turn(self):
        data2 = []
        for row in range(0, self.rows):
            data2.append([self.check(row, col) for col in range(0, self.cols)])
        self.data = data2
