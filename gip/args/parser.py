from itertools import zip_longest
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
        filtered_args = list(
            filter(lambda iarg: iarg[1][-1] == ':', enumerate(args)))
        for (i, arg), next_ in zip_longest(filtered_args, filtered_args[1:]):
            if next_ is None:
                j = len(args)
            else:
                j = next_[0]

            command = args[i][:-1]
            fargs = []
            fkwargs = {}
            for pos in range(i + 1, j):
                key, value = _get_kwargs(args[pos])
                if value is None:
                    fargs.append(key)
                else:
                    fkwargs[key] = value

            if command.find('.') != -1:
                namespace, command = command.split('.')
            else:
                namespace = None
            self.tokens.append(Token(namespace, command, *fargs, **fkwargs))
        return self.tokens

    def get_tokens(self):
        return self.tokens
