import tkinter as tk

root = tk.Tk()
root.title("Hangman")
root.minsize(1000, 690)
root.attributes("-fullscreen", True)
root.config(bg="black")
mainloop = root.mainloop

main = tk.Frame(root, bg="black")
main.place(relx=.5, rely=.5, anchor="center")

hangmanDisplay = tk.Label(main, bg="black", fg="white", anchor="w", justify="left", font=("", 20), padx=100, pady=50)
hangmanDisplay.grid(row=0, column=0, sticky="w")
def update_hangman(text: str, fg: str="white"):
    hangmanDisplay.config(text=text, fg=fg)

right_frame = tk.Frame(main, bg="black")
right_frame.grid(row=0, column=1, sticky="e")

msgLabel = tk.Label(right_frame, text="Guess the number [1 to 30]: ", bg="black", fg="yellow", font=("", 13))
def showmsg(text: str, fg: str="yellow"):
    msgLabel.config(text=text, fg=fg)
msgLabel.pack()

inputGuess = tk.Entry(right_frame, font=("", 13), bg="black", fg="white", insertbackground="white")
inputGuess.pack(pady=50)
inputGuess.focus_set()
def get_guess():
    return inputGuess.get()
def config_onguess_input(onguess_input):
    def handler(evt):
        onguess_input(evt)
        inputGuess.delete(0, "end")
    inputGuess.bind("<Return>", handler)
def disable_guess_input():
    inputGuess.config(state="disabled")