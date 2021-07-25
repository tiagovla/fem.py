import numpy as np


def determinant(J: np.ndarray) -> np.ndarray:

    dim = J.shape[0]
    if dim == 2:
        det = J[0, 0] * J[1][1] - J[0][1] * J[1][0]
    elif dim == 3:
        det = (J[0][0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1]) - J[0][1] *
               (J[1][0] * J[2][2] - J[1][2] * J[2][0]) + J[0][2] *
               (J[1][0] * J[2][1] - J[1][1] * J[2][0]))
    else:
        raise Exception("Not implemented for the given dimension.")

    if np.sum(det == 0) > 0:
        raise Exception("Zero matrix determinant")

    return det


def inverse(J: np.ndarray) -> np.ndarray:

    dim = J.shape[0]
    det = determinant(J)
    inv = np.empty((dim, dim) + J[0][0].shape)

    if dim == 2:
        inv[0, 0] = J[1][1]
        inv[0, 1] = -J[0][1]
        inv[1, 0] = -J[1][0]
        inv[1, 1] = J[0][0]
    elif dim == 3:
        inv[0, 0] = -J[1][2] * J[2][1] + J[1][1] * J[2][2]
        inv[1, 0] = J[1][2] * J[2][0] - J[1][0] * J[2][2]
        inv[2, 0] = -J[1][1] * J[2][0] + J[1][0] * J[2][1]
        inv[0, 1] = J[0][2] * J[2][1] - J[0][1] * J[2][2]
        inv[1, 1] = -J[0][2] * J[2][0] + J[0][0] * J[2][2]
        inv[2, 1] = J[0][1] * J[2][0] - J[0][0] * J[2][1]
        inv[0, 2] = -J[0][2] * J[1][1] + J[0][1] * J[1][2]
        inv[1, 2] = J[0][2] * J[1][0] - J[0][0] * J[1][2]
        inv[2, 2] = -J[0][1] * J[1][0] + J[0][0] * J[1][1]
    else:
        raise Exception("Not implemented for the given dimension.")

    return inv / det
