from abc import abstractmethod, ABCMeta


class AbstractImage(metaclass=ABCMeta):
    shape_accessor = {
        'height': 'H',
        'width': 'W',
        'channel': 'C',
        'depth': 'D',
    }

    def __init__(self, shape_format='HWC'):
        self.shape_format = shape_format

    def __getattr__(self, name):
        assert name not in self.shape_accessor, f'Unknown accessor name:{name}'
        self.shape[self.shape_format.index(self.shape_accessor[name])]

    @property
    @abstractmethod
    def shape(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def channel(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def channel(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def data(self):
        raise NotImplementedError

    @data.setter
    @abstractmethod
    def _(self, src):
        raise NotImplementedError

    @abstractmethod
    def iter_images(self):
        raise NotImplementedError

    @abstractmethod
    def iter_channel(self):
        raise NotImplementedError

    def iter_frames(self):
        return self.iter_images()

    def iter_slices(self, axis=None):
        return self.iter_images()
