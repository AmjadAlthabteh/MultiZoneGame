import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from games import tic_tac_toe, spelling_bee, connect_four, memory_match, hangman
from PIL import Image, ImageTk
import pygame  # For smooth transitions

class MultiGameApp:
    def __init__(self, root):
        pygame.init()
        self.root = root
        self.root.title("Dark Mode Multi-Game Zone")
        self.root.geometry("800x800")
        self.root.configure(bg="#2b2b2b")  # Dark background for a modern look

        # Title Label with a font and spacing
        title_label = tk.Label(root, text="Welcome to Multi-Game Zone!", font=("Helvetica", 30, "bold"), bg="#2b2b2b", fg="#dcdcdc")
        title_label.pack(pady=30)

        # Score Display
        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 18), bg="#2b2b2b", fg="#dcdcdc")
        self.score_label.pack(pady=10)

        # Game Buttons with updated styles and commands
        self.create_game_button("Tic Tac Toe", tic_tac_toe.TicTacToe)
        self.create_game_button("Spelling Bee 🐝", spelling_bee.SpellingBee)
        self.create_game_button("Connect 4", connect_four.ConnectFour)
        self.create_game_button("Memory Match", memory_match.MemoryMatch)
        self.create_game_button("Hangman", hangman.Hangman)

    def create_game_button(self, game_name, game_class):
        button = tk.Button(self.root, text=game_name, font=("Helvetica", 16), width=25, bg="#607d8b", fg="#ffffff",
                           command=lambda: self.launch_game(game_class))
        button.pack(pady=15)

    def launch_game(self, game_class):
        self.fade_out()  # Smooth fade-out transition
        game_window = tk.Toplevel(self.root)
        game = game_class(game_window, self.update_score)
        game.start_game()

    def fade_out(self):
        for alpha in range(100, 0, -5):
            self.root.attributes("-alpha", alpha / 100)
            pygame.time.delay(20)
        self.root.attributes("-alpha", 1)

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")  # Dark theme
    app = MultiGameApp(root)
    root.mainloop()
