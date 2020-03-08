from tkinter import *
from const import Const
from cell_data import CellData


class Window:
    win = Tk()

    def __init__(self, cell_data: CellData):
        self.cell_data = cell_data
        self.cv = Canvas(self.win, width=600, height=400)
        self.cv.pack()

        self.game_loop()
        self.win.mainloop()

    def draw_stage(self):
        data = self.cell_data.data
        self.cv.delete('all')
        for row in range(0, len(data)):
            for col in range(0, len(data[row])):
                if not data[row][col]:
                    continue
                x, y = [col * Const.CELL_SIZE, row * Const.CELL_SIZE]
                self.cv.create_oval(
                    x, y, x + Const.CELL_SIZE, y + Const.CELL_SIZE, fill="red", width=0)

    def game_loop(self):
        self.cell_data.next_turn()
        self.draw_stage()
        self.win.after(300, self.game_loop)
