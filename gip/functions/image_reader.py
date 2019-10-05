from gip.core.function import Function
from gip.core.function_manager import register_function
from gip.core.extensionable import Extensionable
from gip.core.validate_image import ValidateImage
from gip.third_party.get_image_size import get_image_metadata
from pathlib import Path
import imageio


@register_function('load')
class ImageReader(Function, Extensionable):
    def __init__(self, filename: Path):
        """Read image from uri.

        Args:
            filename (Path): A uri will be loaded.
        """

        self.filename = filename
        super().__init__(filename)

    def validate(self):
        assert self.filename.suffix in self._get_extension_names(), \
            f'Unsupported extensions. {self.filename.suffix}'
        meta = get_image_metadata(str(self.filename))

        return ValidateImage(shape=(meta.height, meta.width, None))

    def apply(self):
        func = self._get_extension(self.filename.suffix)
        if func is None:
            return imageio.imread(str(self.filename))
        else:
            return func(str(self.filename))
