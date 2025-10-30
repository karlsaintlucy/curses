# https://www.youtube.com/watch?v=YmaS1e2CxZg&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=12

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

    init_pair(1, COLOR_YELLOW, COLOR_GREEN)
    yellow_on_green: int = color_pair(1)

    init_pair(2, COLOR_BLACK, COLOR_GREEN)
    black_on_green: int = color_pair(2)

    grass: c_void_p = newwin(10, 50, 5, 5)
    grass_panel: c_void_p = new_panel(grass)  # pylint: disable=W0612

    dude: c_void_p = newwin(1, 1, 8, 30)
    wattron(dude, black_on_green | A_BOLD)
    waddstr(dude, "@")
    wattroff(dude, black_on_green | A_BOLD)
    dude_panel: c_void_p = new_panel(dude)  # pylint: disable=W0612

    wbkgd(grass, ".", yellow_on_green)

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
