def _hangman_frames():

    yield """
|======
|    ||
|
|
|
|
|==========
"""

    yield """
|======
|    ||
|    O
|
|
|
|==========
"""

    yield """
|======
|    ||
|    O
|    |
|    |
|
|
"""

    yield """
|======
|    ||
|    O -> Hi
|   \|
|    |
|
|==========
"""

    yield """
|======
|    ||
|    O -> Save me :(
|   \|/
|    |
|
|==========
"""

    yield """
|======
|    ||
|    O -> ...
|   \|/
|    |
|   /
|==========
"""

_frames = list(_hangman_frames())
def next_frame():
    if len(_frames) > 0:
        return _frames.pop(0)
    else:
        return None

correct_guess_won = """
     O -> Your guess is correct!
    \|/
     |
    / \\
"""

incorrect_guess_lost = """
|======
|    ||
|    O -> {number} WAS THE CORRECT NUMB- *rip*
|   \|/
|    |
|   / \\
|==========
"""