from gip.logging import autoinit  # NOQA
import gip.functions
from gip import args


def main():
    parser = args.ArgumentsParser()
    tokens = parser.parse_tokens()

    if len(tokens) == 0:
        tokens.append(args.Token('', 'help', verbose=False))
    gip.core.app.run(tokens)


if __name__ == "__main__":
    main()
