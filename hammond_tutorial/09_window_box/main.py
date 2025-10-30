# https://www.youtube.com/watch?v=Ab18Jlsd-iM&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=10

from ctypes import c_void_p
from functools import wraps
from typing import Callable

from unicurses import *


def curse(func: Callable[[c_void_p], None]):
    @wraps(func)
    def wrapper() -> None:
        stdscr: c_void_p = initscr()

        start_color()
        noecho()
        curs_set(False)
        keypad(stdscr, True)

        func(stdscr)

        endwin()

    return wrapper


@curse
def main(stdscr: c_void_p) -> None:  # pylint: disable=W0613

    window = newwin(3, 25, 3, 3)
    box(window)
    mvwaddstr(window, 1, 1, "Hey there!")

    wnoutrefresh(window)
    doupdate()

    running: bool = True
    while running:
        key: int = wgetch(window)
        if key == 27:  # Esc
            running = False
            break


if __name__ == "__main__":
    main()  # pylint: disable=E1120
