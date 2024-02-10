import tkinter as tk

root = tk.Tk()
root.title("Hangman")
root.config(bg="black")
mainloop = root.mainloop

hangmanDisplay = tk.Label(root, bg="black", fg="white", anchor="w", justify="left", font=("", 30), padx=100, pady=50)
hangmanDisplay.pack()
def update_hangman(text: str, fg: str="white"):
    hangmanDisplay.config(text=text, fg=fg)

tk.Label(root, text="Guess the number [1 to 30]: ", bg="black", fg="yellow", font=("", 13)).pack()

inputGuess = tk.Entry(root, font=("", 13), bg="black", fg="white")
inputGuess.pack(pady=50)