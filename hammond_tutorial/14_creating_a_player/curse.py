from ctypes import c_void_p
from functools import wraps
from typing import Callable

from unicurses import *


def curse(func: Callable[[c_void_p], None]):
    @wraps(func)
    def wrapper() -> None:
        stdscr: c_void_p = initscr()

        start_color()
        noecho()
        curs_set(False)
        keypad(stdscr, True)

        func(stdscr)

        endwin()

    return wrapper
