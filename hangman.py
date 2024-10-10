import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, root, update_score_callback):
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("400x300")
        self.root.configure(bg="#263238")
        self.update_score_callback = update_score_callback
        self.word_list = ["python", "programming", "hangman", "developer"]
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = 6

    def start_game(self):
        self.display_word = tk.StringVar()
        self.update_display_word()
        tk.Label(self.root, text="Hangman", font=("Helvetica", 24, "bold"), bg="#263238", fg="white").pack(pady=10)
        self.word_label = tk.Label(self.root, textvariable=self.display_word, font=("Helvetica", 18), bg="#263238", fg="#f44336")
        self.word_label.pack(pady=5)
        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        tk.Button(self.root, text="Guess", command=self.make_guess, bg="#ff8a65").pack(pady=10)

    def update_display_word(self):
        self.display_word.set(" ".join([letter if letter in self.guessed_letters else "_" for letter in self.word]))

    def make_guess(self):
        guess = self.entry.get().upper()
        if len(guess) == 1 and guess.isalpha():
            self.guessed_letters.add(guess)
            if guess not in self.word:
                self.attempts_left -= 1
            self.update_display_word()
            if all(letter in self.guessed_letters for letter in self.word):
                messagebox.showinfo("Hangman", "You won!")
                self.update_score_callback(15)
