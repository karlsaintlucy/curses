# https://www.youtube.com/watch?v=dliaf1IGBSw&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=11

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

    window_1: c_void_p = newwin(3, 20, 5, 5)
    box(window_1)
    mvwaddstr(window_1, 1, 1, "Hey YouTube!")

    window_2 = newwin(3, 20, 4, 4)
    box(window_2)
    mvwaddstr(window_2, 1, 1, "This is window_2!")

    panel_1: c_void_p = new_panel(window_1)
    panel_2: c_void_p = new_panel(window_2)  # pylint: disable=W0612

    # move_panel(panel_1, 10, 30)
    top_panel(panel_1)

    update_panels()
    doupdate()

    running: bool = True
    while running:
        key: int = getch()
        if key == KEY_ESC:
            running = False
            break


if __name__ == "__main__":
    main()  # pylint: disable=E1120
