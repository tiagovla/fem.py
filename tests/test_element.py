import numpy as np
import pytest

from fem.element.tri import ElementTriP1, ElementTriP2


def test_element_kronecker_property():
    for Element in [ElementTriP1, ElementTriP2]:
        el = Element()
        points = Element.ldoflocs
        phi = el.local_basis(points)
        sum0 = np.sum(phi, axis=0)
        sum1 = np.sum(phi, axis=2)
        assert sum0 == pytest.approx(1, rel=1e-5)
        assert sum1 == pytest.approx(1, rel=1e-5)
