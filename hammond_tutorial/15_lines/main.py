# Python [curses] 15 Lines
# https://www.youtube.com/watch?v=nuzw48H7tdw&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=16

import sys

from ctypes import c_void_p

from unicurses import *

from color import Color
from curse import curse
from player import Player

KEY_ESC: int = 27


@curse
def main(stdscr: c_void_p) -> None:  # pylint: disable=W0613
    if not has_colors():
        sys.exit(1)

    magenta = Color(COLOR_MAGENTA).color_pair

    player: Player = Player(
        stdscr=stdscr,
        body="@",
        foreground=COLOR_RED,
        background=COLOR_BLACK,
        attribute=A_BOLD,
    )

    move(3, 2)

    attron(magenta)

    # vline("|", 10)
    # hline("-", 10)
    vline(ACS_VLINE, 10)
    hline(ACS_HLINE, 10)

    attroff(magenta)

    running: bool = True
    while running:
        key: int = getch()
        if key == KEY_ESC:
            running = False
            break

        player.move(stdscr=stdscr, key=key)


if __name__ == "__main__":
    main()  # pylint: disable=E1120
