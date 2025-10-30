# https://www.youtube.com/watch?v=S09WKA8K9Ek&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=3

from unicurses import *


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    # move(5, 30)
    # addstr("Hello World!")

    # mvaddstr(5, 30, "Hello World!")
    # getch()

    for i in range(50):
        mvaddstr(10, i, "Hello World!")
        getch()

    endwin()


if __name__ == "__main__":
    main()
