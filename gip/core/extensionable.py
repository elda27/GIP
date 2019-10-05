from gip.core.function import Function


class Extensionable:
    def __init_subclass__(cls):
        cls._extensions = {}

    @classmethod
    def _extend(cls, *names):
        def _(klass):
            assert issubclass(klass, Function)
            assert hasattr(klass, '_extensions')

            for name in names:
                assert name in cls._extensions, \
                    f'Registering extension is exist, {name}.'
                cls._extensions[name] = klass
            return klass
        return _

    def _get_extension_names(self):
        for name in self._extensions:
            yield name

    def _get_extension(self, name):
        return self._extennions.get(name)(*self.args, **self.kwargs)
