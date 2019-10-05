from gip import core
from gip.core.function import Function


@core.register_function('as')
class AsVariable(Function):
    _app = core.app

    def __init__(self, name: str, delete: bool = True):
        """Create a variable from top of the stack.

        Args:
            name (str, optional): New name of variable. Defaults to None.
            delete (bool, optional): If true, delete value from the stack. 
                Defaults to True.
        """
        self.name = name
        self.delete = delete
        super().__init__(name, delete)

    def validate(self):
        pass

    def apply(self):
        if self.delete:
            value = self._app.value_stack.pop()
        else:
            value = self._app.value_stack[-1]
        self._app.variable_manager.add(self.name, value)
