from gip import core
from gip.core.function import Function
from gip.core.function_manager import register_function
from gip.core.extensionable import Extensionable
from gip.core.variable import Variable
from pathlib import Path
import imageio


@register_function('save')
class ImageWriter(Function, Extensionable):
    _app = core.app

    def __init__(self, filename: Path, image: Variable = None):
        """Save image to uri.

        Args:
            Function ([type]): [description]
            filename (Path): A uri will be saved.
            image (Variable): A variable of the image. 
                If none, an image uses from stack.
        """
        self.filename = filename
        self.image = image
        super(self, Function).__init__(filename, image)

    def validate(self):
        assert self.filename.suffix in self._get_extension_names(), \
            f'Unsupported extensions. {self.filename.suffix}'

    def apply(self):
        func = self._get_extension(self.filename.suffix)
        image = self.get_image()
        if func is None:
            return imageio.imwrite(str(self.filename), image)
        else:
            return func(str(self.filename), image)

    def get_image(self):
        if self.image is None:
            return self._app.value_stack.pop()
        else:
            return self.image
