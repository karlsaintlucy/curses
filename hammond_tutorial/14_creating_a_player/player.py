from ctypes import c_void_p

from unicurses import *

from color import Color


class Player:  # pylint: disable=C0115,R0902
    def __init__(  # pylint: disable=R0913,R0917
        self,
        stdscr: c_void_p,
        body: str,
        foreground: int = COLOR_WHITE,
        background: int = COLOR_BLACK,
        attribute: int = A_NORMAL,
    ) -> None:
        self._body = body
        self._foreground = foreground
        self._background = background
        self._attribute = attribute

        self._y: int = (getmaxy(stdscr) - 1) // 2
        self._x: int = (getmaxx(stdscr) - 1) // 2
        del stdscr

        self._window: c_void_p = newwin(1, 1, self._y, self._x)
        waddstr(self._window, body)
        self._panel = new_panel(self._window)

        self.set_colors(foreground, background)
        self.show_changes()

    def set_colors(self, foreground: int, background: int) -> None:
        self._color = Color(foreground, background).color_pair

        self._foreground = background
        self._background = background

        wattron(self._window, self._color | self._attribute)
        waddch(self._window, self._body)
        wattroff(self._window, self._color | self._attribute)

    def move(self, stdscr: c_void_p, key: int, motion: int = 1):
        moved: bool = False

        if key == KEY_UP:
            if self._y - motion >= 0:
                moved = True
                self._y -= motion
        elif key == KEY_DOWN:
            if self._y + motion <= getmaxy(stdscr) - 1:
                moved = True
                self._y += motion
        elif key == KEY_LEFT:
            if self._x - motion >= 0:
                moved = True
                self._x -= motion
        elif key == KEY_RIGHT:
            if self._x + motion <= getmaxx(stdscr) - 1:
                moved = True
                self._x += motion

        if moved:
            move_panel(self._panel, self._y, self._x)
            self.show_changes()

        del stdscr

    def show_changes(self) -> None:
        update_panels()
        doupdate()
