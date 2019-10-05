import inspect
from gip.core.function import Function


class FunctionWrapper:
    _empty = inspect._empty

    def __init__(self, klass):
        assert issubclass(klass, Function), \
            'Wrapping function should be derrived Function class'
        self.function = klass
        self.help = klass.__doc__
        self.verbose_help = klass.__init__.__doc__
        self.signature = inspect.signature(klass.__init__)

    def apply(self, *args, **kwargs):
        func = self.function
        return func(*args, **kwargs).apply()

    def validate(self, *args, **kwargs):
        func = self.function
        result = func(*args, **kwargs).validate()
        if not isinstance(result, tuple):
            return result[0], result[1:]
        else:
            return result[0], None

    def get_arg(self, name):
        self.signature.parameters[name]

    @property
    def args(self):
        return self.signature.parameters.keys()

    @property
    def default_args(self):
        for arg in self.signature.parameters.values():
            yield arg.default

    @property
    def arg_types(self):
        for arg in self.signature.parameters.values():
            yield arg.annotation
