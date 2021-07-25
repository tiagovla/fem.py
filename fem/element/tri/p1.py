import numpy as np

from fem.refdom import RefTri

from ..base import ElementH1


class ElementTriP1(ElementH1):
    """Representation of a triangular P1 element."""
    dim = 2
    ndof = 3
    refdom = RefTri
    ldoflocs = np.array([
        [0., 0.],
        [1., 0.],
        [0., 1.],
    ])

    @staticmethod
    def local_basis(Ksi: np.ndarray) -> np.ndarray:
        """Local basis of the element."""
        ksi, nu = Ksi[:, 0], Ksi[:, 1]
        return np.array([
            [1 - ksi - nu],
            [ksi],
            [nu],
        ])

    @staticmethod
    def local_basis_grad(Ksi: np.ndarray) -> np.ndarray:
        """Local gradient basis of the element."""
        return np.repeat(
            np.array([
                [-1., -1.],
                [1., 0.],
                [0., 1.],
            ])[:, :, np.newaxis], Ksi.shape[0], 2)
