# encoding:utf-8
from const import Const
from cell_data import CellData
from random import randint
from window import Window


def main():
    cell_data = CellData(Const.ROWS, Const.COLS)
    window = Window(cell_data)


if __name__ == "__main__":
    main()
