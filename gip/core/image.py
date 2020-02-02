from gip.core.abstract_image import AbstractImage


class Image(AbstractImage):
    def __init__(self, data=None, shape_format='HWC'):
        super().__init__(shape_format)
        self.image_data = data

    def roi_image(self, x, y, width, height):
        h = self.shape_format.index('H')
        w = self.shape_format.index('W')

        slices = [slice(s) for s in self.shape]
        slices[w] = slice(x, x + width)
        slices[h] = slice(y, y + height)

        return Image(
            self.image_data[tuple(slices)],
            shape_format=self.shape_format)

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
