import numpy as np
from mathematica_x.orbits import simulate_two_body

def test_orbit_shape_and_finiteness():
    t, p = simulate_two_body(5.972e24, 7e6, 600, steps=100)
    assert len(t) == 101
    assert p.shape == (101, 3)
    assert np.isfinite(p).all()
