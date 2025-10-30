# https://www.youtube.com/watch?v=kZ2FrAcfZHg&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=7

from unicurses import *

LINE_1_START: tuple[int, int] = (0, 0)


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    start_color()

    # To retain default terminal background,
    # only changing colors of affected text:
    # use_default_colors()

    # Available colors:
    # - COLOR_BLACK
    # - COLOR_BLUE
    # - COLOR_CYAN
    # - COLOR_GREEN
    # - COLOR_MAGENTA
    # - COLOR_RED
    # - COLOR_WHITE
    # - COLOR_YELLOW

    # To *not* specify a color, use -1, e.g.:
    # init_pair(1, COLOR_RED, -1)    # default background color
    # init_pair(1, -1, COLOR_BLACK)  # default foreground color

    init_pair(1, COLOR_RED, COLOR_BLACK)
    red_on_black: int = color_pair(1)

    attron(red_on_black | A_UNDERLINE)
    mvaddstr(*LINE_1_START, "Hello!")
    attroff(red_on_black | A_UNDERLINE)

    getch()
    endwin()


if __name__ == "__main__":
    main()
