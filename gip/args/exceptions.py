

class ArgparseError(Exception):
    def __init__(self, args, position, message):
        self.args = args
        self.position = position
        self.message = message
        super().__init__(f'{args} (pos:{position}): {message}')


class TokenError(Exception):
    def __init__(self, token, message):
        self.token = token
        self.message = message
        super().__init__(f'{message}\n  Token:' + str(token))
