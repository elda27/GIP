from gip.logging import get_logger
from gip.args.exceptions import ArgparseError
from gip.args.token import Token
import sys


def _get_kwargs(arg):
    sep = arg.find('=')
    if sep == -1:
        return (arg, None)
    else:

        return arg[:sep], arg[sep + 1:]


class ArgumentsParser:
    def __init__(self):
        self.tokens = []

    def parse_tokens(self, args=None):
        if args is None:
            args = sys.argv[1:]

        self.tokens = []
        cur_token = None
        for i, arg in enumerate(args):
            sep = arg.find(':')
            if sep == -1:  # This argument is not command.
                if cur_token is None:
                    raise ArgparseError(args, i, 'Wrong format arguments.')
                else:
                    key, value = _get_kwargs(arg)
                    if value is None:  # This argument is usualy argument.
                        cur_token['args'].append(key)
                    else:             # This argument is keyword argument.
                        cur_token['kwargs'][key] = value
                    continue

            command = arg[:sep]

            # Found next command.
            if cur_token is not None and sep != -1:
                token = Token(cur_token['namespace'], cur_token['operation'],
                              *cur_token['args'], **cur_token['kwargs'])
                self.tokens.append(token)
                cur_token = None

            args = []
            kwargs = {}
            option = arg[sep:]
            if not option:  # This argument has argument option
                key, value = _get_kwargs(option)
                if value is None:  # This argument is usualy argument.
                    args.append(key)
                else:             # This argument is keyword argument.
                    kwargs[key] = value

            if command.find('.') != -1:  # This command has namespace
                namespace, operation = command.split('.')
            else:
                namespace = ''
                operation = command

            token = Token(namespace, operation, *args, **kwargs)
            self.tokens.append(token)
        return self.tokens

    def get_tokens(self):
        return self.tokens
