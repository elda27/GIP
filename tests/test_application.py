try:
    import init  # NOQA
except Exception:
    pass
from gip import core
import pytest


@pytest.mark.parametrize(
    'name, args, kwargs, expect_args, expect_kwargs', [
        ('help', [], {'verbose': False}, None, None),
    ]
)
def test_convert_args(name, args, kwargs, expect_args, expect_kwargs):
    if expect_args is None:
        expect_args = args
    if expect_kwargs is None:
        expect_kwargs = kwargs
    app = core.app
    f_wrap = app.function_manager.get_function_wrapper(name)

    conv_args, conv_kwargs = app.convert_args(f_wrap, args, kwargs)
    assert len(conv_args) == len(expect_args)
    assert len(conv_kwargs) == len(expect_kwargs)

    for i, (lhs, rhs) in enumerate(zip(conv_args, expect_args)):
        assert lhs == rhs, \
            f'Failed to convert at {i}th argument.'
    for key in expect_kwargs:
        assert conv_kwargs[key] == expect_kwargs[key], \
            f'Failed to convert at "{key}".'


if __name__ == "__main__":
    pytest.main()
