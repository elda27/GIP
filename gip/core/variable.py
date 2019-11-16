from gip.core.application import app as _app
import re


class Variable:
    _app = _app

    def __init__(self, name=None, instance: bool = False):
        self.name = None
        self.slice = None
        if instance:
            self.raw_value = name
            self.value = name
            return

        self.raw_value = None
        if name is None:
            self.raw_value = self._app.value_stack.pop()
        elif isinstance(name, int):
            self.raw_value = self._app.value_stack.pop(name)
        elif isinstance(name, str):
            self.name, self.slice = self.parse(name)
            self.raw_value = self._app.variable_manager.get(self.name)

        if self.slice is None:
            self.value = self.raw_value[self.slice]
        else:
            self.value = self.raw_value

    def parse(self, string):
        match = re.match(
            r'(?P<var_name>^\D\W+)(\[(?P<key>[\w\d]+)|(?P<index>-?\d?(:-?\d+)?)\])?', string)
        var_name = match.group('var_name')
        index = match.group('index')
        key = match.group('key')
        return var_name, self.get_index(index, key)

    def get_index(self, index, key):
        if index is None:
            if key is not None:
                return key
            else:
                return None

        if index.find(':') == -1:
            range_indices = index.split(':')
            assert all(map(lambda x: x.isdigit(), range_indices)), \
                f'Index should be digit. {range_indices}'
            start, end = map(int, range_indices)
            return slice(int(start), int(end))
        else:
            return int(index)

    @classmethod
    def as_variable(cls, value):
        return cls(value, instance=True)
