from gip import core
from gip.core.function import Function


@core.register_function('list')
class ListFunction(Function):
    _manager = core.function_manager._manager

    def __init__(self):
        """Display list of functions.
        """
        super().__init__()

    def validate(self):
        pass

    def apply(self):
        max_len = max(len(name) for name in self._manager.functions.keys())

        for name, func in self._manager.functions.items():
            f_wrap = core.FunctionWrapper(func)
            if f_wrap.verbose_help is not None:
                help_str = f_wrap.verbose_help
            else:
                help_str = ''
            print('{}: {}'.format(
                name.ljust(min(max_len, 8)),
                help_str[:help_str.find('\n')]))
