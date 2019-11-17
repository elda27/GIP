_converters = {}


def convert(type_, value):
    if type(value) is type_ or issubclass(type(value), type_):
        return value
    if type_ in _converters:
        return _converters[type_](value)
    else:
        return type_(value)


def has_converter(type_):
    return type_ in _converters


def register_converter(type_):
    def _(func):
        assert callable(func)
        assert type_ not in _converters
        _converters[type_] = func
    return _
