# https://www.youtube.com/watch?v=ErxuOYeO--U&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=6

from unicurses import *

LINE_1_START: tuple[int, int] = (0, 0)
LINE_2_START: tuple[int, int] = (1, 0)


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    hello_world: str = "Hello, World!"

    # attron(A_BOLD)
    # mvaddstr(*LINE_1_START, hello_world)
    # attroff(A_BOLD)

    attron(A_UNDERLINE)
    mvaddstr(*LINE_1_START, hello_world)
    attroff(A_UNDERLINE)

    mvaddstr(*LINE_2_START, hello_world)

    getch()
    endwin()


if __name__ == "__main__":
    main()
