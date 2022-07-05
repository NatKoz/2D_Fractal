import warnings
from typing import Tuple

import numpy as np


class Lattice:
    def __init__(self, size: int, center: Tuple[int, int]) -> None:
        self.size = self.__verify_size(size=size)
        self.step = self.size
        self.center = center

        self.max_x = None
        self.min_x = None
        self.max_y = None
        self.min_y = None

        self.__update_min_max()

    def __update_min_max(self) -> None:
        radius = round(self.size / 2)
        self.max_x = self.center[0] + radius
        self.min_x = self.center[0] - radius
        self.max_y = self.center[1] + radius
        self.min_y = self.center[1] - radius

    def __verify_size(self, size) -> int:
        if 0 < size < 3:
            warnings.warn(
                'Size of lattice should be equal or greater than 3. '
                'Setting size to 3',
                RuntimeWarning, stacklevel=9)
            return 3
        return size

    def set_size(self, size: int) -> None:
        self.size = self.__verify_size(size)
        self.__update_min_max()

    def set_center(self, coordinates: Tuple[int, int]) -> None:
        self.center = coordinates
        self.__update_min_max()