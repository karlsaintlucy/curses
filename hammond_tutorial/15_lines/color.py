from unicurses import COLOR_BLACK, init_pair, color_pair


class Color:  # pylint: disable=C0115
    _color_number: int = 1

    def __init__(self, foreground: int, background: int = COLOR_BLACK) -> None:
        self._foreground = foreground
        self._background = background

        init_pair(Color._color_number, self._foreground, self._background)
        self._color_pair: int = color_pair(Color._color_number)

        Color._color_number += 1

    @property
    def foreground(self) -> int:
        return self._foreground

    @property
    def background(self) -> int:
        return self._background

    @property
    def color_pair(self) -> int:
        return self._color_pair
