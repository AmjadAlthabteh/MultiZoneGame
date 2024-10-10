import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, update_score_callback):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.root.configure(bg="#E1F5FE")
        self.update_score_callback = update_score_callback
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

    def start_game(self):
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20, "bold"), width=6, height=3,
                                   bg="#4FC3F7", command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg="black")
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.update_score_callback(15)
                self.root.destroy()
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for positions in win_positions:
            if self.board[positions[0]] == self.board[positions[1]] == self.board[positions[2]] != " ":
                return True
        return False
