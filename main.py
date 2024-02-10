import gui
import man
from random import randrange


number = str(randrange(1, 31))
gui.update_hangman(man.next_frame())

possibilities = list(map(str, range(1, 31)))
incorrect_guesses = []
def on_guess(e):
    guess = gui.get_guess().replace(" ", "")
    if guess not in possibilities:
        gui.showmsg(f"'{guess}' is invalid", "red")
        return
    if guess == number:
        game_won()
    else:
        frame = man.next_frame()
        if not frame:
            game_lost()
            return
        gui.update_hangman(frame)
        if guess not in incorrect_guesses:
            incorrect_guesses.append(guess)
        gui.showmsg(f"Incorrect number(s): {", ".join(incorrect_guesses)}")

def game_won():
    gui.showmsg("Thanks for playing!", "green")
    gui.update_hangman(man.correct_guess_won, "green")
    gui.disable_guess_input()
def game_lost():
    gui.showmsg("Try again!", "yellow")
    gui.update_hangman(man.incorrect_guess_lost.format(number=number), "red")
    gui.disable_guess_input()


gui.config_onguess_input(on_guess)
gui.mainloop()