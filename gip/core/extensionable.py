from gip.core.function import Function
from functools import partial, wraps
from typing import Union, Tuple, List


class Extensionable:
    def __init_subclass__(cls):
        cls._extensions = {}

    @classmethod
    def _extend(cls, *names: Union[Tuple[str], str], **params):
        """Decorator for extend function.

        Args:
            names:  Keys to call extended function. 
            params: This parameters bind function arguments.  
        """
        def _(klass):
            assert issubclass(klass, Function)
            assert hasattr(klass, '_extensions')

            for name in names:
                k = partial(klass, **params)

                # assert name in cls._extensions, \
                #     f'Registering extension is exist, {name}.'
                cls._extensions[name] = k
            return klass
        return _

    def _get_extension_names(self) -> List[str]:
        """Get extensions

        Yields:
            List[str]: Registered extesion keys.
        """
        for name in self._extensions:
            yield name

    def _get_extension(self, name) -> Function:
        return self._extennions.get(name)(*self.args, **self.kwargs)
