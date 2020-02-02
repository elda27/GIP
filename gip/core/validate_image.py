from gip.core.abstract_image import AbstractImage


class ValidateImage(AbstractImage):
    def __init__(self, shape, shape_format='HWC'):
        super().__init__(shape_format)
        self._shape = tuple()

    def roi_image(self, x, y, width, height):
        assert x > 0 and (x + width) < self.width \
            and y > 0 and (y + height) < self.height
        w_index = self.shape_format.find('W')
        h_index = self.shape_format.find('H')
        shape = self.shape
        shape[w_index] = width - x
        shape[h_index] = height - y
        return ValidateImage(shape, shape_format=self.shape_format)

    @property
    def shape(self):
        return self._shape

    @property
    def data(self):
        raise NotImplementedError

    @data.setter
    def _(self, src):
        raise NotImplementedError

    def iter_images(self):
        raise NotImplementedError

    def iter_channel(self):
        raise NotImplementedError

    def iter_frames(self):
        return self.iter_images()

    def iter_slices(self, axis=None):
        return self.iter_images()
