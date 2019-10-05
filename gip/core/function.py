from abc import ABCMeta, abstractmethod


class Function(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        self.name = ''
        self.args = args
        self.kwargs = kwargs
        self.message = None

    def validate(self):
        """Validate input and output

        Returns:
            Any: If not None or returns are multiple, 
                 This function will be returned any value.
        """
        return None

    def has_error(self):
        return self.message is not None

    def clear_error(self):
        self.message = None

    def set_last_error(self, message):
        self.message = message

    def get_last_error(self, message):
        return self.message

    @abstractmethod
    def apply(self):
        """Apply process

        Args:
            image (AbstractImage): input image
        """
        raise NotImplementedError
