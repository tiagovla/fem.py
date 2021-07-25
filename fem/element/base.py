from abc import ABC
from typing import Type

import numpy as np

from fem.refdom import Refdom


class Element(ABC):
    """Base class for an element."""
    dim: int
    ldoflocs: np.ndarray
    refdom: Type[Refdom] = Refdom

    @staticmethod
    def local_basis(Ksi: np.ndarray) -> np.ndarray:
        raise NotImplemented

    @staticmethod
    def local_basis_grad(Ksi: np.ndarray) -> np.ndarray:
        raise NotImplemented


class ElementH1(Element):
    """Base class for an element within the H1 vector space."""


class ElementHCurl(Element):
    """Base class for an element within the H curl vector space."""


class ElementHDiv(Element):
    """Base class for an element within the H div vector space."""
