# https://www.youtube.com/watch?v=sfIOYX11kLc&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=8

from unicurses import *

LINE_1_START: tuple[int, int] = (0, 0)


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr, True)

    getch()
    endwin()


if __name__ == "__main__":
    main()
