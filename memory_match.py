import tkinter as tk
import random

class MemoryMatch:
    def __init__(self, root, update_score_callback):
        self.root = root
        self.root.title("Memory Match")
        self.root.geometry("400x400")
        self.root.configure(bg="#263238")  # Darker background for game
        self.update_score_callback = update_score_callback
        self.cards = [str(i) for i in range(8)] * 2
        self.selected = []
        random.shuffle(self.cards)

    def start_game(self):
        tk.Label(self.root, text="Memory Match!", font=("Helvetica", 18, "bold"), bg="#263238", fg="white").pack(pady=10)
        self.create_grid()

    def create_grid(self):
        for i in range(4):
            for j in range(4):
                card_button = tk.Button(self.root, text="*", width=8, height=4, command=lambda i=i, j=j: self.reveal_card(i, j))
                card_button.grid(row=i, column=j, padx=5, pady=5)
                card_button.card_value = self.cards[i * 4 + j]

    def reveal_card(self, i, j):
        btn = self.root.grid_slaves(row=i, column=j)[0]
        btn.config(text=btn.card_value, state="disabled", disabledforeground="blue")
        self.selected.append(btn)
        if len(self.selected) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        if self.selected[0].card_value == self.selected[1].card_value:
            for btn in self.selected:
                btn.config(bg="green")
            self.update_score_callback(10)
        else:
            for btn in self.selected:
                btn.config(text="*", state="normal")
        self.selected.clear()
