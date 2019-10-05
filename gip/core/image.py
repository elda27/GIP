from gip.core.abstract_image import AbstractImage
import numpy as np


class Image(AbstractImage):
    def __init__(self):
        super().__init__()
        self.image_data = np.array()

    @property
    def shape(self):
        return self.image_data.shape

    @property
    def data(self):
        return self.image_data

    @data.setter
    def _(self, src):
        self.image_data = src
        return self.image_data

    def iter_images(self):
        yield self.image

    def iter_channel(self):
        if len(self.shape) == 3:
            for i in range(self.shape[-1]):
                yield self.data[..., i]
        else:
            yield self.data
