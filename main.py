import tkinter as tk
from class_files.Board import Board
from class_files.Point import Point
import random as rd
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.init_board()
        self.create_left_panel()

    def init_board(self):
        self.right_frame = tk.Frame(self.master, width=100, height=300, bg="red")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.board = Board(self.right_frame, width=300, height=300)

    def create_left_panel(self):
        self.left_frame = tk.Frame(self.master, width=100, height=300, bg="white")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        tk.Label(self.left_frame,
                 text="Number of iterations: ",
                 bg="white").pack(side=tk.TOP, padx=10)

        self.slider_iter = tk.Scale(self.left_frame, from_=10, to=5000,
                                    orient=tk.HORIZONTAL, bg="white")
        self.slider_iter.pack(side=tk.TOP, padx=10)

        tk.Label(self.left_frame,
                 text="Update delay: ",
                 bg="white").pack(side=tk.TOP, padx=10)

        self.slider_delay = tk.Scale(self.left_frame, from_=0, to=1,
                                     resolution=0.1, orient=tk.HORIZONTAL,
                                     bg="white")
        self.slider_delay.pack(side=tk.TOP, padx=10)

        self.start_button = tk.Button(self.left_frame,
                                      text="Start the simulation",
                                      command=self.start_simulation)
        self.start_button.pack(side=tk.TOP, padx=10, pady=10)

        self.clear_button = tk.Button(self.left_frame,
                                      text="Clear the board",
                                      command=self.board.clear_board)
        self.clear_button.pack(side=tk.TOP, padx=10, pady=10)

        self.msg_box = tk.Label(self.left_frame)
        self.msg_box.pack(side=tk.TOP, padx=10)

    def start_simulation(self):
        if self.board.starting_triangle_ready():
            print("Ready")
            for n in range(int(self.slider_iter.get())):
                result = rd.randint(1, 6)
                self.board.draw_point_from_throw(result)
                self.board.update()
                time.sleep(self.slider_delay.get())
                self.show_message(f"Iteration {n}: Got {result}")
            self.show_message("Simulation done")
        else:
            self.show_message("Please add more points")

    def show_message(self, text: str):
        self.msg_box.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chaos game")
    app = Application(master=root)
    app.mainloop()

