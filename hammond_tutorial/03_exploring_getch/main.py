# https://www.youtube.com/watch?v=OBg7cCPhBC4&list=PL1H1sBF1VAKXLJ3cHisqjy4nGYDMqYIzo&index=4

from unicurses import *


def main() -> None:

    stdscr = initscr()  # pylint: disable=W0612

    maxx = getmaxx(stdscr)

    running = True

    while running:
        move(0, 0)
        key: int = getch()

        # if key == 27:  # ESC
        if key == 10:  # Enter
            running = False
            break

        move(10, 0)
        addstr(f"Keycode was {key} and the key was {chr(key)!r}.".ljust(maxx))

    # getch()

    endwin()


if __name__ == "__main__":
    main()
