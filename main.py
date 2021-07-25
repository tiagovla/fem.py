import meshio
import numpy as np
from matplotlib import pyplot as plt
from scipy.sparse.linalg import spsolve

import geogen
from fem.assembler.basis import BasisCell
from fem.assembler.wave import AssemblerWave
from fem.element.line import ElementLineL1, ElementLineL2, ElementLineL3
from fem.element.tri import ElementTriP1, ElementTriP2, ElementTriP3
from fem.mapping import MappingIsoparametric
from fem.mesh import Mesh2d
from fem.solver import SolverEnforceDirichlet

geo = geogen.Geometry("triangle6", "test", lc=2e-2)
geo.generate_mesh()

mesh = Mesh2d.from_gmsh("test.msh")
asm = AssemblerWave()

x = mesh.x
el = ElementTriP2
el_line = ElementLineL2
conn = mesh.conn[el]
xm = np.mean(x[conn, :], axis=1)

dirichlet_lines = mesh.sets["Dirichlet"][el_line]
bc_nodes = np.unique(mesh.conn[el_line][dirichlet_lines])
bc_values = np.zeros(bc_nodes.shape)

f = 2 * np.pi**2 * np.sin(xm[:, 0] * np.pi) * np.sin(xm[:, 1] * np.pi)
px = np.ones(conn.shape[0])
py = np.ones(conn.shape[0])
q = np.zeros(conn.shape[0])

basis = BasisCell(mesh, el)
A, b = asm.assemble(basis, px, py, q, f)

u = SolverEnforceDirichlet.solve(A, b, bc_nodes, bc_values)


def u_ref_func(x):
    return np.sin(np.pi * x[:, 0]) * np.sin(np.pi * x[:, 1])


u_ref = u_ref_func(x)
fig, (ax0, ax1) = plt.subplots(1, 2)
ax0.tripcolor(x[:, 0], x[:, 1], u, cmap="jet")
ax1.tripcolor(x[:, 0], x[:, 1], u_ref, cmap="jet")
plt.show()
