

class Token:
    def __init__(self, namespace, operation, *args, **kwargs):
        self.operation = operation
        self.namespace = namespace
        self.args = args
        self.kwargs = kwargs

    @property
    def command(self):
        if self.namespace:
            return f'{self.namespace}.{self.operation}'
        else:
            return self.operation

    def __str__(self):
        return f'{self.command}:{self.args}, {self.kwargs}'
