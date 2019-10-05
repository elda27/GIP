from gip.core.converter import convert


class VariableManager:
    def __init__(self):
        self.variables = {}

    def add(self, name, value):
        self.variables[name] = value

    def get(self, name, value=None):
        return self.variables.get(name, value)

    def try_cast(self, name, type):
        value = self.variables[name]
        try:
            return convert(type, value)
        except Exception:
            return None

    def has_variable(self, name):
        return name in self.variables
