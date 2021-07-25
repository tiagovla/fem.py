import numpy as np
import pytest

from fem.element.tri import ElementTriP1, ElementTriP2
from fem.mapping import MappingIsoparametric


def test_mapping_node_function_mapping_tri_p1():
    el = ElementTriP1()
    mp = MappingIsoparametric(el)
    ksie = np.array([[1 / 3, 1 / 3]])
    xe = np.array([[0, 0], [0, 1], [1, 0]])
    res = mp.map(xe, ksie)
    assert res == pytest.approx(1 / 3, rel=1e-5)


def test_mapping_node_function_mapping_tri_p2():
    el = ElementTriP2()
    mp = MappingIsoparametric(el)
    ksie = np.array([[1 / 3, 1 / 3]])
    xe = el.ldoflocs
    res = mp.map(xe, ksie)
    assert res.flatten() == pytest.approx(1 / 3, rel=1e-5)
