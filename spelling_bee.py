import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class SpellingBee:
    def __init__(self, root, update_score_callback):
        self.root = root
        self.root.title("Spelling Bee")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFFDD0")  # Light yellow background
        self.update_score_callback = update_score_callback
        self.word_list = ["honey", "flower", "bee", "nectar", "garden", "pollen"]
        self.current_word = random.choice(self.word_list)

    def start_game(self):
        tk.Label(self.root, text="Spell the word from the letters:", font=("Helvetica", 16, "bold"), bg="#FFFDD0").pack(pady=15)

        # Display bee image
        bee_image = Image.open("assets/bee.png")
        bee_image = bee_image.resize((90, 90), Image.ANTIALIAS)
        bee_photo = ImageTk.PhotoImage(bee_image)
        tk.Label(self.root, image=bee_photo, bg="#FFFDD0").pack()
        self.root.image = bee_photo  # Keep a reference to avoid garbage collection

        # Scrambled letters from the selected word
        letters = tk.Label(self.root, text=" ".join(random.sample(self.current_word, len(self.current_word))),
                           font=("Helvetica", 20, "bold"), bg="#FFFDD0")
        letters.pack(pady=5)

        # Input field for the player's answer
        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        # Submit button to check the answer
        submit_button = tk.Button(self.root, text="Submit", command=self.check_spelling, bg="#FFD700")
        submit_button.pack(pady=10)

    def check_spelling(self):
        if self.entry.get().lower() == self.current_word:
            messagebox.showinfo("Spelling Bee", "Correct!")
            self.update_score_callback(10)  # Add points for a correct answer
            self.root.destroy()
        else:
            messagebox.showerror("Spelling Bee", "Try Again!")
