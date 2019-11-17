from gip import core
from gip.functions.concat.concat import Concat
from gip.core.validate_image import ValidateImage
import numpy as np


@core.register_function('concat_image')
@Concat._extend('concat_image_align_square', aligns=['width', 'height'])
@Concat._extend('concat_image_align_width', aligns=['width'])
@Concat._extend('concat_image_align_height', aligns=['height'])
class ConcatImage(Concat):
    def __init__(self, *args, aligns, **kwargs):
        self.aligns = aligns
        self.block_shape = None
        super().__init__(*args, aligns=aligns, **kwargs)

    def validate(self):
        block_shape = {}
        for align in self.aligns:
            block_shape.setdefault(align, []).append(
                max([getattr(i, align) for i in self.images]))
        self.block_shape = block_shape

        return ValidateImage(
            self.get_output_shape(),
            self.images[0].shape_format)

    def get_output_shape(self):
        bx, by = self.stack_shape
        return self.block_shape[0] * bx, self.block_shape[1] * by

    def apply(self):
        output = self.alloc_output(self.get_output_shape())
        bw, bh = self.block_shape
        for bx, by in zip(range(self.stack_shape[0]), range(self.stack_shape[1])):
            img = self.images[by * bw + bx]
            w = img.width
            h = img.height
            np.core.multiarray.copyto(
                output.roi_image(bx * bw, by * bh, w, h).data,
                img.data, mode='unsafe'
            )
        return output
