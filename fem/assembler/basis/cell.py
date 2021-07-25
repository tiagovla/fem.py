from __future__ import annotations

from typing import Type

import numpy as np

from fem.element.base import Element
from fem.mapping import MappingIsoparametric
from fem.mapping.base import Mapping
from fem.mesh.base import Mesh
from fem.quadrature import Quadrature, get_quadrature

from .base import Basis


class BasisCell(Basis):
    """Represent a cell basis."""
    def __init__(self,
                 mesh: Mesh,
                 elem: Element | Type[Element],
                 elem_subset: np.ndarray | None = None,
                 mapping: Mapping | None = None,
                 int_order: int | None = None,
                 quadrature: Quadrature | None = None):
        self.mesh = mesh
        self.elem = elem
        self.elem_subset = elem_subset
        self.mapping = mapping if mapping else MappingIsoparametric(self.elem)
        self.int_order = int_order if int_order else 4
        self.quadrature = quadrature if quadrature else get_quadrature(
            self.elem.refdom, self.int_order)
