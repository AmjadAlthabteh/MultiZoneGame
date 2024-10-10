import tkinter as tk
from tkinter import messagebox
import time

class ConnectFour:
    def __init__(self, root, update_score_callback):
        self.root = root
        self.root.title("Connect 4")
        self.root.geometry("700x600")
        self.root.configure(bg="#37474f")  # Dark background
        self.update_score_callback = update_score_callback
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.current_player = "Red"
        self.create_grid()

    def create_grid(self):
        # Create a grid of buttons for gameplay
        for row in range(6):
            for col in range(7):
                btn = tk.Button(self.root, text=" ", width=10, height=4, bg="#546e7a",
                                command=lambda r=row, c=col: self.drop_disc(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.board[row][col] = btn

    def drop_disc(self, row, col):
        # Find the lowest available slot in the column
        for i in range(5, -1, -1):
            if self.board[i][col]["text"] == " ":
                self.board[i][col]["text"] = "O" if self.current_player == "Red" else "X"
                self.board[i][col]["fg"] = "#ff5252" if self.current_player == "Red" else "#42a5f5"
                self.animate_drop(i, col)  # Animation effect
                if self.check_winner():
                    self.update_score_callback(20)
                    messagebox.showinfo("Connect 4", f"{self.current_player} wins!")
                    self.root.destroy()
                self.current_player = "Blue" if self.current_player == "Red" else "Red"
                break

    def animate_drop(self, row, col):
        # Simulate a "drop" by displaying it one row at a time
        for i in range(row+1):
            self.board[i][col].config(bg="#ff5252" if self.current_player == "Red" else "#42a5f5")
            self.root.update()
            time.sleep(0.1)

    def check_winner(self):
        # Check for horizontal, vertical, and diagonal matches
        for row in range(6):
            for col in range(7):
                if self.check_line(row, col, 1, 0) or self.check_line(row, col, 0, 1) or \
                   self.check_line(row, col, 1, 1) or self.check_line(row, col, 1, -1):
                    return True
        return False

    def check_line(self, row, col, delta_x, delta_y):
        try:
            if self.board[row][col]["text"] == " ":
                return False
            for i in range(1, 4):
                if self.board[row][col]["text"] != self.board[row + i * delta_x][col + i * delta_y]["text"]:
                    return False
            return True
        except IndexError:
            return False

