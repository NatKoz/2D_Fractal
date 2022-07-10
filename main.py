from area import Area
from diffusion_limited_aggregation import DiffusionLimitedAggregation

if __name__ == '__main__':
    area = Area(size=20, lattice_size=0)
    dla = DiffusionLimitedAggregation(area=area, particles_count=10)
    dla.simulate()
    area.plot()