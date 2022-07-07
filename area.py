from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt

from lattice import Lattice


class Area:
    def __init__(self, size: int = (100, 100),
                 lattice_size: int = 0) -> None:
        self.size = size
        self.matrix = np.zeros((self.size, self.size))
        self.center = (round(self.size / 2), round(self.size / 2))

        self.lattice = None
        if lattice_size > 0:
            self.lattice = Lattice(size=lattice_size, center=self.center)

    def get_center(self) -> Tuple[int, int]:
        return self.center

    def get_size(self) -> int:
        return self.size

    def plot(self) -> None:
        plt.ylim(0, self.size - 1)
        plt.xlim(0, self.size - 1)
        plt.imshow(self.matrix)
        plt.show()

    def stick_particle(self, coordinates: Tuple[int, int]) -> None:
        self.matrix[coordinates[0]][coordinates[1]] = 1

    def particle_exists(self, coordinates: Tuple[int, int]) -> bool:
        return bool(self.matrix[coordinates[0]][coordinates[1]])

    def increase_lattice_size(self) -> None:
        new_lattice_size = self.lattice.size + self.lattice.step
        if new_lattice_size > self.size - 1:
            new_lattice_size = self.size - 1
        self.lattice.set_size(new_lattice_size)
    
    def get_random_boundary_coordinate(self) -> Tuple[int, int]:
        if self.lattice:
            return self.lattice.get_random_boundary_coordinate()

        else:
            boundary = np.random.randint(1, 1)
