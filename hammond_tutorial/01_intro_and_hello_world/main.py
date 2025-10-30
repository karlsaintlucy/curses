# https://www.youtube.com/watch?v=4s_wHUNCHK0&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=2

from unicurses import *


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    addstr("Hello World!")
    getch()

    endwin()


if __name__ == "__main__":
    main()
