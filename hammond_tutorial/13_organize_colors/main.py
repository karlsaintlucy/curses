# https://www.youtube.com/watch?v=YXFZxQKQYOU&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=14

import sys

from ctypes import c_void_p

from unicurses import *

from color import Color
from curse import curse

KEY_ESC: int = 27


@curse
def main(stdscr: c_void_p) -> None:  # pylint: disable=W0613
    if not has_colors():
        sys.exit(1)

    red = Color(COLOR_RED).color_pair
    blue = Color(COLOR_BLUE).color_pair

    move(0, 0)

    attron(red)
    addstr("This is in red!")
    attroff(red)

    move(1, 0)

    attron(blue)
    addstr("This is in blue!")
    attroff(blue)

    running: bool = True
    while running:
        key: int = getch()
        if key == KEY_ESC:
            running = False
            break


if __name__ == "__main__":
    main()  # pylint: disable=E1120
