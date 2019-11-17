from gip.core.function_wrapper import FunctionWrapper
from gip.core.function import Function


class FunctionManager:
    def __init__(self):
        self.functions = {}

    def register(self, name: str, klass: Function):
        assert name not in self.functions, \
            f'Duplicating function name of {name}'
        self.functions[name] = klass

    def get_function_wrapper(self, name: str):
        assert name in self.functions, f'Unknown function {name}'
        return FunctionWrapper(self.functions[name])

    def has_function(self, name: str):
        return name in self.functions

    def create(self, name: str, *args, **kwargs):
        return self.functions[name](*args, **kwargs)


_manager = FunctionManager()


def register_function(name):
    def _(klass):
        klass._name = name
        _manager.register(name, klass)
        return klass
    return _
