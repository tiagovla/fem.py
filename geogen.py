import gmsh


class ElementType:
    def __init__(self, name, line_type, order=1, recombine=False):
        self.name = name
        self.line_type = line_type
        self.order = order
        self.recombine = recombine

    @classmethod
    def from_name(cls, name):
        if name == "triangle":
            return cls(name, "line", 1, False)
        elif name == "triangle6":
            return cls(name, "line3", 2, False)
        elif name == "triangle10":
            return cls(name, "line4", 3, False)
        elif name == "quad":
            return cls(name, "line", 1, True)
        elif name == "quad9":
            return cls(name, "line3", 2, True)
        else:
            raise Exception("Element name not found.")

    def elem_options(self, gmsh):
        if self.recombine:
            gmsh.model.mesh.recombine()
        gmsh.model.mesh.setOrder(self.order)
        # if self.order > 1:
        #     gmsh.model.mesh.optimize("HighOrder")


def define_mesh_test(lc):
    p1 = gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
    p2 = gmsh.model.geo.addPoint(1, 0, 0, lc, 2)
    p3 = gmsh.model.geo.addPoint(1, 1, 0, lc, 3)
    p4 = gmsh.model.geo.addPoint(0, 1, 0, lc, 4)

    gmsh.model.geo.addLine(p1, p2, 1)
    gmsh.model.geo.addLine(p2, p3, 2)
    gmsh.model.geo.addLine(p3, p4, 3)
    gmsh.model.geo.addLine(p4, p1, 4)

    gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
    gmsh.model.geo.addPlaneSurface([1], 1)
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(1, [1, 2, 3, 4], 11)
    gmsh.model.addPhysicalGroup(2, [1], 12)
    gmsh.model.setPhysicalName(1, 11, "Dirichlet")
    gmsh.model.setPhysicalName(2, 12, "Region_0")

    gmsh.model.mesh.generate(2)


def define_mesh_blind_test(lc):
    a = 0.1

    p1 = gmsh.model.geo.add_point(0, 0, 0, lc, 1)
    p2 = gmsh.model.geo.add_point(5 * a, 0, 0, lc, 2)
    p3 = gmsh.model.geo.add_point(5 * a, 5 * a, 0, lc, 3)
    p4 = gmsh.model.geo.add_point(0, 5 * a, 0, lc, 4)

    gmsh.model.geo.add_line(p1, p2, 1)
    gmsh.model.geo.add_line(p2, p3, 2)
    gmsh.model.geo.add_line(p3, p4, 3)
    gmsh.model.geo.add_line(p4, p1, 4)

    gmsh.model.geo.add_curve_loop([1, 2, 3, 4], 1)
    gmsh.model.geo.addPlaneSurface([1], 1)

    gmsh.model.geo.synchronize()
    gmsh.model.add_physical_group(1, [4], 11)
    gmsh.model.add_physical_group(1, [2], 12)
    gmsh.model.add_physical_group(2, [1], 21)
    gmsh.model.set_physical_name(1, 11, "dirichlet_1")
    gmsh.model.set_physical_name(1, 12, "dirichlet_2")
    gmsh.model.set_physical_name(2, 21, "material")


def define_mesh_blind(lc):
    a = 0.1
    b = 0.122026
    p1 = gmsh.model.geo.add_point(0, 0, 0, 0.1 * lc, 1)
    p2 = gmsh.model.geo.add_point(a, 0, 0, 0.1 * lc, 2)
    p3 = gmsh.model.geo.add_point(b, 0, 0, 0.1 * lc, 3)
    p4 = gmsh.model.geo.add_point(5 * a, 0, 0, lc, 4)
    p5 = gmsh.model.geo.add_point(5 * a, 5 * a, 0, lc, 5)
    p6 = gmsh.model.geo.add_point(0, 5 * a, 0, 0.1 * lc, 6)
    p7 = gmsh.model.geo.add_point(0, b, 0, 0.1 * lc, 7)
    p8 = gmsh.model.geo.add_point(0, a, 0, 0.1 * lc, 8)

    gmsh.model.geo.add_line(p1, p2, 1)
    gmsh.model.geo.add_line(p2, p3, 2)
    gmsh.model.geo.add_line(p3, p4, 3)
    gmsh.model.geo.add_line(p4, p5, 4)
    gmsh.model.geo.add_line(p5, p6, 5)
    gmsh.model.geo.add_line(p6, p7, 6)
    gmsh.model.geo.add_line(p7, p8, 7)
    gmsh.model.geo.add_line(p8, p1, 8)

    gmsh.model.geo.add_circle_arc(p2, p1, p8, 9)
    gmsh.model.geo.add_circle_arc(p3, p1, p7, 10)

    gmsh.model.geo.add_curve_loop([1, 9, 8], 1)
    gmsh.model.geo.add_curve_loop([2, 10, 7, -9], 2)
    gmsh.model.geo.add_curve_loop([3, 4, 5, 6, -10], 3)

    gmsh.model.geo.addPlaneSurface([3], 1)
    gmsh.model.geo.addPlaneSurface([2], 2)
    gmsh.model.geo.addPlaneSurface([1], 3)

    gmsh.model.geo.synchronize()

    gmsh.model.add_physical_group(1, [6, 7, 8], 11)
    gmsh.model.add_physical_group(1, [4], 12)
    gmsh.model.add_physical_group(2, [1, 3], 21)
    gmsh.model.add_physical_group(2, [2], 22)
    gmsh.model.set_physical_name(1, 11, "dirichlet_1")
    gmsh.model.set_physical_name(1, 12, "dirichlet_2")
    gmsh.model.set_physical_name(2, 21, "vacum")
    gmsh.model.set_physical_name(2, 22, "material")


def define_mesh_cond(lc):
    a = 0.05
    b = 0.055
    p1 = gmsh.model.geo.add_point(0, 0, 0, 0.3 * lc, 1)
    p2 = gmsh.model.geo.add_point(a, 0, 0, 0.01 * lc, 2)
    p3 = gmsh.model.geo.add_point(b, 0, 0, 0.01 * lc, 3)
    p4 = gmsh.model.geo.add_point(6 * a, 0, 0, lc, 4)
    p5 = gmsh.model.geo.add_point(6 * a, 6 * a, 0, lc, 5)
    p6 = gmsh.model.geo.add_point(0, 6 * a, 0, 0.2 * lc, 6)
    p7 = gmsh.model.geo.add_point(0, b, 0, 0.01 * lc, 7)
    p8 = gmsh.model.geo.add_point(0, a, 0, 0.01 * lc, 8)

    gmsh.model.geo.add_line(p1, p2, 1)
    gmsh.model.geo.add_line(p2, p3, 2)
    gmsh.model.geo.add_line(p3, p4, 3)
    gmsh.model.geo.add_line(p4, p5, 4)
    gmsh.model.geo.add_line(p5, p6, 5)
    gmsh.model.geo.add_line(p6, p7, 6)
    gmsh.model.geo.add_line(p7, p8, 7)
    gmsh.model.geo.add_line(p8, p1, 8)

    gmsh.model.geo.add_circle_arc(p2, p1, p8, 9)
    gmsh.model.geo.add_circle_arc(p3, p1, p7, 10)

    gmsh.model.geo.add_curve_loop([1, 9, 8], 1)
    gmsh.model.geo.add_curve_loop([2, 10, 7, -9], 2)
    gmsh.model.geo.add_curve_loop([3, 4, 5, 6, -10], 3)

    gmsh.model.geo.addPlaneSurface([3], 1)
    gmsh.model.geo.addPlaneSurface([2], 2)
    gmsh.model.geo.addPlaneSurface([1], 3)

    gmsh.model.geo.synchronize()

    gmsh.model.add_physical_group(1, [6, 7, 8], 11)
    gmsh.model.add_physical_group(1, [4], 12)
    gmsh.model.add_physical_group(2, [1, 3], 21)
    gmsh.model.add_physical_group(2, [2], 22)
    gmsh.model.set_physical_name(1, 11, "dirichlet_1")
    gmsh.model.set_physical_name(1, 12, "dirichlet_2")
    gmsh.model.set_physical_name(2, 21, "vacum")
    gmsh.model.set_physical_name(2, 22, "material")


class Geometry:
    def __init__(self, elem_type, filename, lc=1e-2):
        self.elem_type = ElementType.from_name(elem_type)
        self.filename = filename
        self.lc = lc

    def start(self):
        gmsh.initialize()
        # gmsh.option.setNumber("General.Verbosity", 2)
        gmsh.model.add(self.filename)
        if self.elem_type.recombine:
            gmsh.option.set_number("Mesh.Algorithm", 9)
        # gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 3)  # or 3

    def define_mesh(self):
        if self.filename == "blind":
            define_mesh_blind(self.lc)
        elif self.filename == "cond":
            define_mesh_cond(self.lc)
        elif self.filename == "test":
            define_mesh_test(self.lc)
        elif self.filename == "blind_test":
            define_mesh_blind_test(self.lc)

    def generate_mesh(self):
        self.start()
        self.define_mesh()

        gmsh.model.mesh.generate(2)
        # gmsh.model.mesh.optimize("Laplace2D")
        self.elem_type.elem_options(gmsh)
        gmsh.write(f"{self.filename}.msh")

        # gmsh.fltk.run()
        self.close()

    def close(self):
        gmsh.finalize()
