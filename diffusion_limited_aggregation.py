from area import Area

class DiffusionLimitedAggregation:
    def __init__(self, area: Area, particles_count: int = 10) -> None:
        self.area = area
        self.x, self.y = self.area.get_random_boundary_coordinate()
        self.particles_count = particles_count
        self.remaining_particles = self.particles_count