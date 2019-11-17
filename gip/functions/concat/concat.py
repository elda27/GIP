from gip import core
from gip.core.function import Function
from gip.core.variable import Variable
from gip.core.abstract_image import AbstractImage
from gip.core.image import Image
from gip.core.color import Color
from gip.image_utils.fill_image import fill_image
import numpy as np


@core.register_function('concat')
class Concat(Function, core.Extensionable):
    def __init__(
            self, image: Variable, *images: Variable, stack: str = 'horz',
            mode: str = 'square', image_type: str = None,
            background: Color = Color('k')
    ):
        """Concat images

        Args:
            image (int, Variable): First element of images or number of images 
                to concat from stack.
            images (Variable): Images will be concatenated.
            stack (str, optional): Stacking method, {'horz', 'vert', 'MxN'}. 
                About 'MxN', a shape of stacking and M or N should be digit.
                Defaults to 'horz'.
            mode (str, optional): Alignment size method of the 
                difference sizes. Defaults to 'square'.
            image_type (str, optional): Concatenation will be applied 
                this image type. Reserved parameter. 
                Defaults to None.
            background (Color, optional): Padding color 
        """
        self.images = self.get_images_from_variable(image, *images)
        self.stack = stack
        self.mode = f'concat_image_{mode}'
        self.image_type = 'image'
        self.stack_shape = self.get_stack(self.stack)
        self.background = background

        assert self.mode in self._get_extension_names(), \
            f'Unknown concatenation mode: {self.mode}'
        self._concat_impl = self._get_extension(self.mode)

        super().__init__(
            image, *image,
            stack=stack, mode=mode, image_type=image_type)

    def validate(self):
        x, y = self.get_stack(self.stack)
        assert all([isinstance(i, AbstractImage) for i in self.images]), \
            'Variable should be derrived AbstractImage.' \
            'Actual flags: {}'.format(
                [isinstance(i, AbstractImage) for i in self.images])
        assert x is not None and y is not None, \
            f'Stacking shape x or y should be integer. Actual: {self.stack}'

        return self._concat_impl.validate()

    def get_images_from_variable(self, *images: Variable) -> AbstractImage:
        return [i.value for i in images]

    def get_stack(self, stack):
        x, y = stack.split('x')
        x = int(x) if x.isdigit() else None
        y = int(x) if y.isdigit() else None
        return x, y

    def alloc_output(self, shape):
        img = Image(np.empty(shape))
        return fill_image(img, self.background.rgb)

    def apply(self):
        return self._concat_impl.apply()
