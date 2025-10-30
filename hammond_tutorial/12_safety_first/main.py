# https://www.youtube.com/watch?v=85RMrF4gsRI&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=13

from ctypes import c_void_p
from functools import wraps
from typing import Callable

from unicurses import *

KEY_ESC: int = 27


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

    init_pair(2, COLOR_GREEN, COLOR_BLACK)
    green = color_pair(2)

    init_pair(3, COLOR_RED,   COLOR_BLACK)
    red = color_pair(3)

    color: int = green if has_colors() else red

    attron(color | A_BOLD)
    addstr(
        f"You {'*do*' if has_colors() else '*don\'t*'} "
        "have colors available in your terminal.",
    )
    attroff(color | A_BOLD)

    running: bool = True
    while running:
        key: int = getch()
        if key == KEY_ESC:
            running = False
            break


if __name__ == "__main__":
    main()  # pylint: disable=E1120
