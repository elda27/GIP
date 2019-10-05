
from gip.core.variable_manager import VariableManager
from gip.core.function_manager import _manager as _function_manager
from gip.core.converter import convert
from gip.logging import get_logger


class Application:
    _logger = get_logger(__name__)

    def __init__(self):
        self.variable_manager = VariableManager()
        self.function_manager = _function_manager
        self.value_stack = []
        self.last_error = None

    def run(self, tokens):
        # Validation process
        for token in tokens:
            if not self.validate(token.command, *token.args, **token.kwargs):
                pos = tokens.index(token)
                self._logger.error(
                    f'Failed to validate at {pos}th token.\n'
                    f'{token}\n{self.last_error}')
                return

        # Run process
        for token in tokens:
            try:
                self.invoke(token.command, *token.args, **token.kwargs)
            except Exception as e:
                pos = tokens.index(token)
                self._logger.error(
                    f'Position: {pos}, {token}\n'
                    f'Uncaught exception: {type(e)}\n'
                    f'{e}')
                return

    def invoke(self, name, *args, **kwargs):
        return self.invoke_impl(name, False, *args, **kwargs)

    def validate(self, name, *args, **kwargs):
        return self.invoke_impl(name, True, *args, **kwargs)

    def invoke_impl(self, name, validate, *args, **kwargs):
        f_wrap = self.function_manager.get_function_wrapper(name)
        result = self.convert_args(f_wrap, args, kwargs)
        if result is None:
            raise self.last_error

        conv_args, conv_kwargs = result

        self.last_func = f_wrap.function(*conv_args, **conv_kwargs)
        if validate:
            result = self.last_func.apply()
        else:
            result = self.last_func.validate()

        if result is not None:
            self.value_stack.append(result)

        return not self.last_func.has_error()

    def convert_args(self, f_wrap, args, kwargs):
        conv_args = []
        conv_kwargs = {}
        for i, (arg_type, arg) in enumerate(zip(f_wrap.arg_types, args)):
            value = self.get_variable(arg)
            if arg_type is f_wrap._empty:
                conv_args.append(value)
                continue

            try:
                conv_args.append(convert(arg_type, value))
            except Exception:
                arg_name = list(f_wrap.args)[i]
                self.set_last_error_message(
                    'Failed to convert argument.\n'
                    f'Position:{i}, Arg name: {arg_name}, Type: {arg_type}')
                return None

        for arg_type, (arg_name, arg) in zip(f_wrap.arg_types, kwargs.items()):
            value = self.get_variable(arg)
            if arg_type is f_wrap._empty:
                conv_kwargs[arg_name] = value
                continue

            try:
                conv_kwargs[arg_name] = convert(arg_type, value)
            except Exception:
                arg_name = f_wrap.get_arg(arg_name)
                self.set_last_error_message(
                    'Failed to convert keyword argument.\n'
                    f'Arg name: {arg_name}, Type: {arg_type}')
                return None
        return conv_args, conv_kwargs

    def get_variable(self, name):
        if self.variable_manager.has_variable(name):
            return self.variable_manager.get(name)
        else:
            return name

    def set_last_error(self, e):
        self.last_error = e

    def set_last_error_message(self, msg):
        self.set_last_error(Exception(msg))


app = Application()  # NOQA
