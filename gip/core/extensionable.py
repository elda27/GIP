from gip.core.function import Function
from functools import partial, wraps


class Extensionable:
    def __init_subclass__(cls):
        cls._extensions = {}

    @classmethod
    def _extend(cls, *names, **params):
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

    def _get_extension_names(self):
        for name in self._extensions:
            yield name

    def _get_extension(self, name):
        return self._extennions.get(name)(*self.args, **self.kwargs)
