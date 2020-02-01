try:
    import init  # NOQA
except Exception:
    pass
from gip import args
import pytest


@pytest.mark.parametrize(
    'input_args, correct_tokens', [
        (
            ['help:', 'help', 'verbose=False', 'load:', 'image.png', 'output=false'],
            [args.Token(None, 'help', 'help', verbose='False'),
             args.Token(None, 'load', 'image.png', output='false')]
        ),
    ]
)
def test_parse_args(input_args, correct_tokens):
    parser = args.ArgumentsParser()
    tokens = parser.parse_tokens(input_args)
    assert len(tokens) == len(correct_tokens)

    for token, correct_token in zip(tokens, correct_tokens):
        assert token.namespace == correct_token.namespace
        assert token.operation == correct_token.operation
        assert token.args == correct_token.args
        assert token.kwargs == correct_token.kwargs


if __name__ == "__main__":
    pytest.main()
