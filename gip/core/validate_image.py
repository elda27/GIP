from gip.core.abstract_image import AbstractImage


class ValidateImage(AbstractImage):
    def __init__(self, shape, shape_format='HWC'):
        super().__init__(shape_format)
        self._shape = tuple()

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
