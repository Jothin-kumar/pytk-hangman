import gui
from random import randrange


number = str(randrange(1, 31))

possibilities = list(map(str, range(1, 31)))
incorrect_guesses = []
def on_guess(e):
    guess = gui.get_guess().replace(" ", "")
    if guess not in possibilities:
        gui.showmsg(f"'{guess}' is invalid", "red")
        return
    if guess == number:
        print("Yay")
        gui.showmsg("Thanks for playing!", "green")
    else:
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
        gui.showmsg(f"Incorrect number(s): {", ".join(incorrect_guesses)}")

gui.config_onguess_input(on_guess)
gui.mainloop()