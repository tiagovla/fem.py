from __future__ import annotations

from typing import Callable, Tuple

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, lil_matrix

from fem.assembler.basis import BasisCell
from fem.mesh.base import Mesh
from fem.utils.functions import determinant, inverse

from .base import Assembler


def local_element_matrix(
        basis: BasisCell, xe: np.ndarray, pxe: float | Callable,
        pye: float | Callable, qe: float | Callable,
        fe: float | Callable) -> Tuple[np.ndarray, np.ndarray]:

    mapping = basis.mapping
    gauss_p, gauss_w = basis.quadrature

    if isinstance(pxe, float) and isinstance(pye, float):
        pp = np.diag([pxe, pye])

    phi = mapping.elem.local_basis(gauss_p)
    phi_grad = mapping.elem.local_basis_grad(gauss_p)

    jacb = mapping.jacobian(xe, gauss_p)
    det_jacb = determinant(jacb)
    inv_jacb = inverse(jacb)
    B = np.einsum("ijk,jlk->ilk", phi_grad, inv_jacb)
    A1 = np.einsum("ijm,jk,lkm,m->il", B, pp, B, gauss_w * det_jacb)
    b = fe * np.einsum("ijk,k", phi, gauss_w * det_jacb)

    return (A1, b)


class AssemblerWave(Assembler):
    def assemble(self, basis: BasisCell, px: np.ndarray, py: np.ndarray,
                 q: np.ndarray,
                 f: np.ndarray) -> Tuple[lil_matrix, lil_matrix]:
        x = basis.mesh.x
        conn = basis.mesh.conn[basis.elem]

        A = lil_matrix((x.shape[0], x.shape[0]))
        b = lil_matrix((x.shape[0], 1))
        for e in range(conn.shape[0]):
            conn_e = conn[e, :]
            x_e = x[conn_e, :]
            Ae, be = local_element_matrix(basis, x_e, px[e], py[e], q[e], f[e])
            ind_x, ind_y = np.meshgrid(conn_e, conn_e, indexing="ij")
            A[ind_x, ind_y] = A[ind_x, ind_y] + Ae
            b[conn_e] = b[conn_e] + be

        return A, b
