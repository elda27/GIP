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
                self.print_command(f_wrap)
                print('-' * 80)
                self.print_verbose(f_wrap)
            else:
                self.print_command(f_wrap)
                print(f_wrap.verbose_help[:f_wrap.verbose_help.find('\n')])

    def print_usage(self):
        print(
            'usage: gip <command>: [arg] ... [<keyword>=<value>] ...\n\n'
            'need list of command, type "gip list:".\n'
            'or need more help about any command, '
            'please type "gip help: <command name>".')

    def print_command(self, f_wrap):
        # for param in f_wrap.signature.parameters:
        command_help = f'{f_wrap.function._name}: '
        for key, param in list(f_wrap.signature.parameters.items())[1:]:
            if param.default is f_wrap._empty:
                command_help += f'<{param}> '
            else:
                command_help += f'[{param}] '

        print(f'Usage: {command_help}')

    def print_verbose(self, f_wrap):
        lines = f_wrap.verbose_help.split('\n')
        pos = 0
        for i, s in enumerate(lines[2]):
            if s != ' ':
                pos = i
                break
        args = map(lambda x: x[pos:], lines[2:])
        print('\n'.join(args))
