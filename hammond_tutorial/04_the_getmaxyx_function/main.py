# https://www.youtube.com/watch?v=3JMF3xYF7VU&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=5

from unicurses import *


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    maxy, maxx = getmaxyx(stdscr)

    mvaddstr(maxy//2, maxx//2, "@")
    getch()

    endwin()


if __name__ == "__main__":
    main()
