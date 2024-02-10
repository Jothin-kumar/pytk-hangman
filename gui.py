import tkinter as tk

root = tk.Tk()
root.title("Hangman")
root.config(bg="black")
mainloop = root.mainloop

hangmanDisplay = tk.Label(root, bg="black", fg="white", anchor="w", justify="left", font=("", 30), padx=100, pady=50)
hangmanDisplay.pack()
def update_hangman(text: str, fg: str="white"):
    hangmanDisplay.config(text=text, fg=fg)

msgLabel = tk.Label(root, text="Guess the number [1 to 30]: ", bg="black", fg="yellow", font=("", 13))
def showmsg(text: str, fg: str="yellow"):
    msgLabel.config(text=text, fg=fg)
msgLabel.pack()

inputGuess = tk.Entry(root, font=("", 13), bg="black", fg="white")
inputGuess.pack(pady=50)
def get_guess():
    return inputGuess.get()
def config_onguess_input(onguess_input):
    inputGuess.bind("<Return>", onguess_input)
def disable_guess_input():
    inputGuess.config(state="disabled")