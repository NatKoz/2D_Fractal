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
