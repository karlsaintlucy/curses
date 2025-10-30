# https://www.youtube.com/watch?v=j8XcCXp1tBs&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=9

from unicurses import *

WINDOW_1_DIMENSIONS: tuple[int, int] = (2, 25)
WINDOW_1_BEGIN_YX: tuple[int, int] = (3, 5)

WINDOW_2_DIMENSIONS: tuple[int, int] = (2, 25)
WINDOW_2_BEGIN_YX: tuple[int, int] = (3, 30)


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr, True)

    window_1 = newwin(*WINDOW_1_DIMENSIONS, *WINDOW_1_BEGIN_YX)
    # box(window_1)
    waddstr(window_1, "Hello, World!")

    window_2 = newwin(*WINDOW_2_DIMENSIONS, *WINDOW_2_BEGIN_YX)
    # box(window_2)
    waddstr(window_2, "Hello, World again!")

    wnoutrefresh(window_1)
    wnoutrefresh(window_2)
    doupdate()

    running = True
    while running:
        key = wgetch(window_1)

        # wnoutrefresh(window_1)
        # wnoutrefresh(window_2)
        # doupdate()

        if key == 27:  # Esc
            running = False
            break

    endwin()


if __name__ == "__main__":
    main()
