from area import Area
from typing import Tuple, List
import random

class DiffusionLimitedAggregation:
    def __init__(self, area: Area, particles_count: int = 100) -> None:
        self.area = area
        self.x, self.y = self.area.get_random_boundary_coordinate()
        self.particles_count = particles_count
        self.remaining_particles = self.particles_count

    def __get_random_direction(self) -> Tuple[int, int]:
        return random.choice(((1, 0),
                              (0, 1),
                              (-1, 0),
                              (0, -1),
                              (1, 1),
                              (1, -1),
                              (-1, -1),
                              (-1, 1)
                              ))
    
    def __get_random_step(self) -> List[int]:
        direction = self.__get_random_direction()
        particle_coordinates = [self.x + direction[0],
                                self.y + direction[1]]

        if self.area.lattice:
            if particle_coordinates[0] > self.area.lattice.max_x - 1:
                particle_coordinates[0] = self.area.lattice.max_x - 1
            if particle_coordinates[0] < self.area.lattice.min_x + 1:
                particle_coordinates[0] = self.area.lattice.min_x + 1
            if particle_coordinates[1] > self.area.lattice.max_y - 1:
                particle_coordinates[1] = self.area.lattice.max_y - 1
            if particle_coordinates[1] < self.area.lattice.min_y + 1:
                particle_coordinates[1] = self.area.lattice.min_y + 1

        else:
            if particle_coordinates[0] < 0:
                particle_coordinates[0] = 0
            if particle_coordinates[1] < 0:
                particle_coordinates[1] = 0
            if particle_coordinates[0] > self.area.get_size() - 1:
                particle_coordinates[0] = self.area.get_size() - 1
            if particle_coordinates[1] > self.area.get_size() - 1:
                particle_coordinates[1] = self.area.get_size() - 1

        return particle_coordinates