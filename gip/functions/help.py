from gip import core
from gip.core.function import Function


@core.register_function('help')
class Help(Function):
    _manager = core.function_manager._manager

    def __init__(self, func_name: str = None, verbose: bool = False):
        """Display help message.

        Args:
            func_name (str, optional): Function name. Defaults to None.
            verbose (bool, optional): If true, print verbose message. 
                Defaults to False.
        """
        self.func_name = func_name
        self.verbose = verbose
        super().__init__(func_name, verbose=verbose)

    def validate(self):
        if self.func_name is None:
            return
        assert self._manager.has_function(self.func_name), \
            f'Unknown function: {self.func_name}'

    def apply(self):
        if self.func_name is None:
            self.print_usage()
        else:
            f_wrap = self._manager.get_function_wrapper(self.func_name)
            if self.verbose:
                self.print_verbose(f_wrap)
            else:
                self.print_simple(f_wrap)

    def print_usage(self):
        print(
            'usage: gip <command>: [arg] ... [<keyword>=<value>] ...\n\n'
            'need list of command, type "gip list:".\n'
            'or need more help about any command, '
            'please type "gip help: <command name>".')

    def print_simple(self, f_wrap):
        print(str(f_wrap.signature))

    def print_verbose(self, f_wrap):
        print(f_wrap.verbose_help)
