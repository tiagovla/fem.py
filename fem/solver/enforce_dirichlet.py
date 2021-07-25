import numpy as np
from scipy.sparse.linalg import spsolve

from .base import Solver


class SolverEnforceDirichlet(Solver):
    @staticmethod
    def solve(A, b, bc_nodes: np.ndarray, bc_values: np.ndarray):
        n_nodes = A.shape[0]
        b = b - A[:, bc_nodes] @ bc_values[:, np.newaxis]
        A.rows = np.delete(A.rows, bc_nodes, 0)
        A.data = np.delete(A.data, bc_nodes, 0)
        A._shape = (A.shape[0] - len(bc_nodes), A.shape[1])
        mask = np.delete(np.arange(A.shape[1]), bc_nodes)
        A = A.tocsc()[:, mask]
        b = b[mask, :]

        u = np.zeros(n_nodes)

        u[mask] = spsolve(A, b)
        u[bc_nodes] = bc_values

        return u
