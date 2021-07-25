from __future__ import annotations

import meshio

from fem.element.line import ElementLineL1, ElementLineL2, ElementLineL3
from fem.element.tri import ElementTriP1, ElementTriP2, ElementTriP3

from .base import Mesh

MAPPING_GMSH_FEM = {
    "line": ElementLineL1,
    "line3": ElementLineL2,
    "line4": ElementLineL3,
    "triangle": ElementTriP1,
    "triangle6": ElementTriP2,
    "triangle10": ElementTriP3
}


class Mesh2d(Mesh):
    """Represent a 2d Mesh."""
    def __init__(self, x, conn: dict | None = None, sets: dict | None = None):
        self.x = x
        self.conn = conn if conn else {}
        self.sets = sets if sets else {}
        self.data = {}

    @classmethod
    def from_gmsh(cls, filename) -> Mesh2d:
        """Generate a mesh from a gmsh file."""
        mesh = meshio.read(filename)
        x = mesh.points[:, :2]
        conn = {MAPPING_GMSH_FEM[k]: v for k, v in mesh.cells_dict.items()}
        sets = {
            k: {
                MAPPING_GMSH_FEM[kk]: vv
            }
            for k, v in mesh.cell_sets_dict.items() for kk, vv in v.items()
        }
        ret_mesh = cls(x, conn)
        ret_mesh.sets = sets
        return ret_mesh
