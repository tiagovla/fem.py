import numpy as np

from fem.refdom import RefTri

from ..base import ElementH1


class ElementTriP2(ElementH1):
    """Representation of a triangular P2 element."""
    dim = 2
    ndof = 3
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
        # yapf: disable
        return np.array([[(1.-2.*ksi-2.*nu)*(1.-ksi-nu)],
            [ksi*(2.*ksi-1.)],
            [nu*(2.*nu-1.)],
            [4.*ksi*(1.-ksi-nu)],
            [4.*ksi*nu],
            [4.*nu*(1.-ksi-nu)]])
        # yapf: enable

    @staticmethod
    def local_basis_grad(Ksi):
        """Local gradient basis of the element."""
        ksi, nu = Ksi[:, 0], Ksi[:, 1]
        return np.array([
            [-3. + 4. * ksi + 4. * nu, -3. + 4. * ksi + 4. * nu],
            [4. * ksi - 1., 0. * ksi],
            [0. * ksi, 4. * nu - 1.],
            [4. - 8. * ksi - 4. * nu, -4. * ksi],
            [4. * nu, 4. * ksi],
            [-4. * nu, 4. - 8. * nu - 4. * ksi],
        ])
