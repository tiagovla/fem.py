import numpy as np

from ..base import ElementH1


class ElementLineL3(ElementH1):
    """Representation of a line L3 element."""
    ndof = 2
    ldoflocs = np.array([
        [0.],
        [1.],
    ])

    @staticmethod
    def local_basis(Ksi: np.ndarray) -> np.ndarray:
        """Local basis of the element."""
        ksi = Ksi[:, 0]
        return np.array([
            [1 - ksi],
            [ksi],
        ])

    @staticmethod
    def local_basis_grad(Ksi: np.ndarray) -> np.ndarray:
        """Local gradient basis of the element."""
        return np.repeat(
            np.array([
                [-1.],
                [1.],
            ])[:, :, np.newaxis], Ksi.shape[0], 1)