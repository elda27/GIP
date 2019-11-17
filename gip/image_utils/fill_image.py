from gip.core.image import Image
from gip.core.abstract_image import AbstractImage
from gip.core.color import Color
import numpy as np


def fill_image(image: AbstractImage, color: Color) -> AbstractImage:
    if isinstance(image, np.array):
        image = Image(image)

    if not isinstance(color, Color):
        color = Color(color)

    channel_axis = image.shape_format.index('C')

    if channel_axis == 1:
        np.multiarray.copyto(image.data, color.gray, casting='unsafe')
    else:
        for f, c in zip(image.iter_channel(), color.rgb):
            np.multiarray.copyto(f, c)
    return image
