import tkinter as tk
from tkinter import messagebox
import random

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")

        # Increase initial window size
        master.geometry("600x500")  # Width x Height

        self.words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
        self.word = random.choice(self.words_to_guess)
        self.length = len(self.word)
        self.count = 0
        self.limit = 5
        self.display = list('_' * self.length)
        self.already_guessed = []

        self.name = tk.StringVar()
        self.guess = tk.StringVar()
        self.hangman_art = tk.StringVar()
        self.word_display = tk.StringVar(value=" ".join(self.display))
        self.guesses_remaining = tk.StringVar(value=f"Guesses Remaining: {self.limit - self.count}")
        self.guessed_letters = tk.StringVar(value=f"Guessed Letters: {', '.join(self.already_guessed)}")

        self.create_widgets()

    def create_widgets(self):
        # Welcome Label and Name Entry
        tk.Label(self.master, text="Welcome to Hangman!", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.master, text="Enter your name:", font=("Arial", 12)).pack()
        name_entry = tk.Entry(self.master, textvariable=self.name, font=("Arial", 12))
        name_entry.pack(pady=5)
        tk.Button(self.master, text="Start Game", command=self.start_game, font=("Arial", 12)).pack(pady=10)

    def start_game(self):
        self.game_window = tk.Toplevel(self.master)
        self.game_window.title("Playing Hangman")
        self.game_window.geometry("600x500") # Increase game window size as well

        tk.Label(self.game_window, text=f"Hello {self.name.get()}! Good luck!", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.game_window, textvariable=self.hangman_art, font=("Courier", 20)).pack(pady=10)
        tk.Label(self.game_window, textvariable=self.word_display, font=("Arial", 28)).pack(pady=10)
        tk.Label(self.game_window, textvariable=self.guesses_remaining, font=("Arial", 12)).pack(pady=5)
        tk.Label(self.game_window, textvariable=self.guessed_letters, font=("Arial", 12)).pack(pady=5)

        guess_entry = tk.Entry(self.game_window, textvariable=self.guess, font=("Arial", 12))
        guess_entry.pack(pady=5)
        guess_button = tk.Button(self.game_window, text="Guess Letter", command=self.hangman, font=("Arial", 12))
        guess_button.pack(pady=10)

        self.update_hangman_art()

    def update_hangman_art(self):
        hangman_stages = [
            "  _____\n |     \n |     \n |     \n |     \n_|_____",
            "  _____\n |   | \n |     \n |     \n |     \n_|_____",
            "  _____\n |   | \n |   O \n |     \n |     \n_|_____",
            "  _____\n |   | \n |   O \n |   | \n |     \n_|_____",
            "  _____\n |   | \n |   O \n |  /|\ \n |     \n_|_____",
            "  _____\n |   | \n |   O \n |  /|\ \n |  / \ \n_|_____"
        ]
        self.hangman_art.set(hangman_stages[self.count] if self.count < len(hangman_stages) else hangman_stages[-1])

    def hangman(self):
        guess = self.guess.get().strip().lower()
        self.guess.set("") # Clear the entry field

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.already_guessed:
            messagebox.showinfo("Already Guessed", "You have already guessed that letter. Try another.")
            return

        if guess in self.word:
            self.already_guessed.append(guess)
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display[i] = guess
            self.word_display.set(" ".join(self.display))
            self.guessed_letters.set(f"Guessed Letters: {', '.join(self.already_guessed)}")
            if "_" not in self.display:
                messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
                self.play_again()
        else:
            self.count += 1
            self.update_hangman_art()
            self.guesses_remaining.set(f"Guesses Remaining: {self.limit - self.count}")
            self.already_guessed.append(guess)
            self.guessed_letters.set(f"Guessed Letters: {', '.join(self.already_guessed)}")
            if self.count == self.limit:
                messagebox.showinfo("Game Over", f"You ran out of guesses! The word was: {self.word}")
                self.play_again()

    def play_again(self):
        play = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play:
            self.word = random.choice(self.words_to_guess)
            self.length = len(self.word)
            self.count = 0
            self.display = list('_' * self.length)
            self.already_guessed = []
            self.word_display.set(" ".join(self.display))
            self.guesses_remaining.set(f"Guesses Remaining: {self.limit - self.count}")
            self.guessed_letters.set(f"Guessed Letters: {', '.join(self.already_guessed)}")
            self.update_hangman_art()
        else:
            self.game_window.destroy()
            messagebox.showinfo("Thanks!", "Thanks For Playing! We expect you back again!")
            self.master.destroy()

root = tk.Tk()
game = HangmanGUI(root)
root.mainloop()