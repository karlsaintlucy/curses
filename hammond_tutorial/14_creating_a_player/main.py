# Python [curses] 14 Creating a "Player"
# https://www.youtube.com/watch?v=YgG53FJgSPU&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=15

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

    white_on_black = Color(COLOR_WHITE, COLOR_BLACK).color_pair
    wbkgd(stdscr, " ", white_on_black)

    player: Player = Player(
        stdscr=stdscr,
        body="@",
        foreground=COLOR_RED,
        attribute=A_BOLD,
    )

    running: bool = True
    while running:
        key: int = getch()
        if key == KEY_ESC:
            running = False
            break

        player.move(stdscr=stdscr, key=key)


if __name__ == "__main__":
    main()  # pylint: disable=E1120
