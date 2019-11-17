
def code_to_color(code):
    assert len(code) in (4, 5, 7, 9), f'Bad format color code: {code}'
    if len(code) == 4 or len(code) == 5:  # "#RGB" or "#RGBA"
        return tuple(map(lambda x: int(x, 16) * 17, code[1:]))
    elif len(code) == 7 or len(code) == 9:  # "#RRGGBB" or "#RRGGBBAA"
        return tuple(map(lambda x, y: int(x + y, 16), code[::1], code[1::1]))


def color_to_code(color):
    code = '#'
    for c in color:
        code += str(hex(c))
    return code


colormap = {
    'k': (0, 0, 0),
    'black': (0, 0, 0),
    'r': (255, 0, 0),
    'red': (255, 0, 0),
    'g': (0, 255, 0),
    'green': (0, 255, 0),
    'b': (0, 0, 255),
    'blue': (0, 0, 255),
    'w': (255, 255, 255),
    'white': (255, 255, 255),
}


def lookup_colormap(color):
    return colormap[color]


class Color:
    def __init__(self, rgb):
        assert isinstance(rgb, (str, list, tuple))
        if isinstance(rgb, str):
            if rgb[0] == '#':
                self.rgb = code_to_color(rgb)
            else:
                self.rgb = lookup_colormap(rgb)
        elif isinstance(rgb, (list, tuple)):
            self.rgb = tuple(rgb)

    @property
    def code(self):
        return color_to_code(self.rgb)

    @property
    def gray(self):
        return int(
            0.2126 * self.rgb[0] +
            0.7152 * self.rgb[1] +
            0.0722 * self.rgb[2])
