from __future__ import annotations

from typing import Type

import numpy as np

from fem.element.base import Element
from fem.utils.functions import determinant, inverse

from .base import Mapping


class MappingIsoparametric(Mapping):
    def __init__(self, elem: Element | Type[Element]):
        self.elem = elem
        self.dim = self.elem.ldoflocs.shape[1]

    def map(self, x_e: np.ndarray, ksi_e: np.ndarray) -> np.ndarray:
        phi = self.elem.local_basis(ksi_e)
        return np.einsum("ji,jkl", x_e, phi)

    def map_grad(self, x_e: np.ndarray, ksi_e: np.ndarray) -> np.ndarray:
        phi_grad = self.elem.local_basis_grad(ksi_e)
        return np.einsum("ji,jkl", x_e, phi_grad)

    def jacobian(self, x_e: np.ndarray, ksi_e: np.ndarray) -> np.ndarray:
        return self.map_grad(x_e, ksi_e)
