import numpy as np

from fem.refdom import RefTri

from ..base import ElementH1


class ElementTriP3(ElementH1):
    """Representation of a triangular P2 element."""
    ndof = 10
    refdom = RefTri
    ldoflocs = np.array([
        [0., 0.],
        [1., 0.],
        [0., 1.],
        [0.5, 0.],
        [0.5, 0.5],
        [0., .5],
    ])

    @staticmethod
    def local_basis(Ksi):
        """Local basis of the element."""

        ksi, nu = Ksi[:, 0], Ksi[:, 1]

        return np.array(
            [[
                -(1 / 2) * (-1 + nu + ksi) * (-2 + 3 * nu + 3 * ksi) *
                (-1 + 3 * nu + 3 * ksi)
            ], [1 / 2 * ksi * (-2 + 3 * ksi) * (-1 + 3 * ksi)],
             [1 / 2 * nu * (-2 + 3 * nu) * (-1 + 3 * nu)],
             [9 / 2 * ksi * (-1 + nu + ksi) * (-2 + 3 * nu + 3 * ksi)],
             [-(9 / 2) * ksi * (-1 + nu + ksi) * (-1 + 3 * ksi)],
             [9 / 2 * nu * ksi * (-1 + 3 * ksi)],
             [9 / 2 * nu * (-1 + 3 * nu) * ksi],
             [-(9 / 2) * nu * (-1 + 3 * nu) * (-1 + nu + ksi)],
             [9 / 2 * nu * (-1 + nu + ksi) * (-2 + 3 * nu + 3 * ksi)],
             [-27 * nu * ksi * (-1 + nu + ksi)]])

    @staticmethod
    def local_basis_grad(Ksi):
        """Local gradient basis of the element."""

        ksi, nu = Ksi[:, 0], Ksi[:, 1]
        return np.array([
            [
                1 / 2 * (-11 - 27 * nu**2 + nu *
                         (36 - 54 * ksi) + 36 * ksi - 27 * ksi**2),
                1 / 2 * (-11 - 27 * nu**2 + nu *
                         (36 - 54 * ksi) + 36 * ksi - 27 * ksi**2)
            ],
            [1 - 9 * ksi + (27 * ksi**2) / 2, 0 * ksi],
            [0 * ksi, 1 - 9 * nu + (27 * nu**2) / 2],
            [
                9 / 2 * (2 + 3 * nu**2 - 10 * ksi + 9 * ksi**2 + nu *
                         (-5 + 12 * ksi)),
                9 / 2 * ksi * (-5 + 6 * nu + 6 * ksi)
            ],
            [
                -(9 / 2) * (1 - 8 * ksi + 9 * ksi**2 + nu * (-1 + 6 * ksi)),
                -(9 / 2) * ksi * (-1 + 3 * ksi)
            ],
            [9 / 2 * nu * (-1 + 6 * ksi), 9 / 2 * ksi * (-1 + 3 * ksi)],
            [9 / 2 * nu * (-1 + 3 * nu), 9 / 2 * (-1 + 6 * nu) * ksi],
            [
                -(9 / 2) * nu * (-1 + 3 * nu),
                -(9 / 2) * (1 + 9 * nu**2 - ksi + nu * (-8 + 6 * ksi))
            ],
            [
                9 / 2 * nu * (-5 + 6 * nu + 6 * ksi),
                9 / 2 * (2 + 9 * nu**2 - 5 * ksi + 3 * ksi**2 + 2 * nu *
                         (-5 + 6 * ksi))
            ],
            [-27 * nu * (-1 + nu + 2 * ksi), -27 * ksi * (-1 + 2 * nu + ksi)],
        ])
