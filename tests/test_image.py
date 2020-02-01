try:
    import init  # NOQA
except Exception:
    pass
from gip import core
import pytest
import numpy as np


@pytest.mark.parametrize(
    'image_type', [
        core.Image
    ]
)
def test_instance(image_type):
    try:
        _ = image_type()
    except Exception:
        for f_name, f_obj in core.AbstractImage.__dict__.items():
            if not hasattr(f_obj, '__isabstractmethod__'):
                continue
            if f_obj.__isabstractmethod__ and f_name not in image_type.__dict__:
                print(f'{f_name} is abstractmethod but not implemented.')
        raise


# @pytest.mark.parametrize(
#     'mapped_shape', [
#         {'width': 480, 'height': 640, 'channel': 6, },
#         {'width': 430, 'channel': 1, 'height': 240, },
#         {'channel': 1, 'width': 480, 'height': 640, },
#         {'height': 240, 'width': 480, 'channel': 3, },
#     ]
# )
# def test_accessor(mapped_shape):
#     image = core.Image(shape_format=''.join(
#         map(lambda x: x[0].upper(), mapped_shape.keys())))
#     image.data = np.zeros(mapped_shape.values())

#     for key, size in mapped_shape.items():
#         assert getattr(image, key) == size


if __name__ == "__main__":
    pytest.main()
