from gip import core
from gip.functions.concat.concat import Concat
from gip.core.validate_image import ValidateImage
from typing import List
import numpy as np


# @core.register_function('concat_image')
@Concat._extend()
class ConcatImage(Concat):
    align_methods = {
        'left': lambda x, s: 0,
        'center': lambda x, s: (s - x) // 2,
        'right': lambda x, s: (s - x),
    }

    def __init__(self, *args, **kwargs):
        self.__doc__ = Concat.__doc__
        self.block_shape = None
        super().__init__(*args, **kwargs)

        align_pos = self.align.find('|')
        if align_pos < 0:
            width_align = self.align
            height_align = self.align
        else:
            width_align = self.align[:align_pos]
            height_align = self.align[align_pos + 1:]
        self.width_align_method = self.align_methods[width_align]
        self.height_align_method = self.align_methods[height_align]

    def validate(self):
        block_shape = {}
        for align in self.aligns:  # Compute maximum size of images
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
                output.roi_image(
                    bx * bw + self.width_align_method(w, bw),
                    by * bh + self.height_align_method(h, bh),
                    w, h
                ).data,
                img.data, mode='unsafe'
            )
        return output
