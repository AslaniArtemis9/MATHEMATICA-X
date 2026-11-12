import numpy as np
import pytest
from mathematica_x.orbits import simulate_two_body

def test_orbit_shape_and_finiteness():
    t, p = simulate_two_body(5.972e24, 7e6, 600, steps=100)
    assert len(t) == 101
    assert p.shape == (101, 3)
    assert np.isfinite(p).all()
    assert t[0] == 0 and t[-1] == 600

def test_circular_orbit_radius_is_reasonably_stable():
    _, p = simulate_two_body(5.972e24, 7e6, 600, steps=4000)
    radii = np.linalg.norm(p, axis=1)
    assert np.max(np.abs(radii - 7e6)) / 7e6 < 1e-4

def test_rejects_invalid_inputs():
    with pytest.raises(ValueError): simulate_two_body(-1, 7e6, 600)
    with pytest.raises(ValueError): simulate_two_body(5.972e24, 7e6, 600, steps=0)
