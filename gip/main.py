from gip.logging import autoinit  # NOQA
import gip.functions
from gip import args
from gip import version

__version__ = version.__version__


def main():
    parser = args.ArgumentsParser()
    tokens = parser.parse_tokens()

    if len(tokens) == 0:
        tokens.append(args.Token('', 'help', verbose=False))
    gip.core.app.run(tokens)
