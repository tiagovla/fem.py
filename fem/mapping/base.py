import numpy as np


class Mapping:
    """Represent a base mapping class."""
    def map(self, x_e: np.ndarray, ksi_e: np.ndarray) -> np.ndarray:
        raise NotImplemented
