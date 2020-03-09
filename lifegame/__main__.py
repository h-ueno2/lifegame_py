# encoding:utf-8
from const import Const
from cell_data import CellData
from window import Window

if __name__ == "__main__":
    cell_data = CellData(Const.ROWS, Const.COLS)
    window = Window(cell_data)
